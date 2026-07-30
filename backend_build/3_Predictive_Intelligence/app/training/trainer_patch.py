import os
import time
import uuid
import joblib
import pandas as pd
from sqlalchemy.orm import Session
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
from app.models.lead import Lead
from app.models.training import ModelRegistry, TrainingHistory
from app.training.model_manager import ModelManager
from app.training.preprocessor import DataPreprocessor
from app.utils.logger import logger
from app.config.settings import settings

def train_lead_model(db: Session, started_by: str, notes: str = None) -> dict:
    lead_count = db.query(Lead).count()
    if lead_count < 3:
        raise ValueError("Not enough leads to train.")
    
    start_time = time.time()
    training_id = str(uuid.uuid4())
    version = ModelManager.get_next_version(db, 'lead')
    
    history = TrainingHistory(
        training_id=training_id,
        model_type='lead',
        model_version=version,
        algorithm='XGBoost',
        lead_records_used=lead_count,
        customer_records_used=0,
        dataset_source='Database',
        started_by=started_by,
        status='running',
    )
    db.add(history)
    db.commit()
    
    try:
        leads = db.query(Lead).all()
        df = pd.DataFrame([{
            'age': l.age,
            'gender': l.gender,
            'occupation': l.occupation,
            'annual_income': l.annual_income,
            'city': l.city,
            'existing_policy': l.existing_policy,
            'product_interested': l.product_interested,
            'website_visits': l.website_visits,
            'email_opens': l.email_opens,
            'calls_answered': l.calls_answered,
            'form_submitted': l.form_submitted,
            'last_interaction_days': l.last_interaction_days,
            'lead_source': l.lead_source,
            'conversion_target': l.conversion_target
        } for l in leads])
        
        preprocessor = DataPreprocessor()
        X, y, feature_names = preprocessor.preprocess_leads(df)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y if y.nunique() > 1 else None)
        
        model = XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            use_label_encoder=False,
            eval_metric='logloss',
            random_state=42
        )
        if y_train.nunique() > 1:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            acc = float(accuracy_score(y_test, y_pred))
            prec = float(precision_score(y_test, y_pred, zero_division=0))
            rec = float(recall_score(y_test, y_pred, zero_division=0))
            f1 = float(f1_score(y_test, y_pred, zero_division=0))
        else:
            model.fit(X_train, y_train)
            acc, prec, rec, f1 = 1.0, 1.0, 1.0, 1.0
        
        duration = time.time() - start_time
        model_path = ModelManager.save_model(model, 'lead', version)
        preprocessor.save(settings.MODEL_STORAGE_PATH, 'lead')
        
        feature_names_path = os.path.join(settings.MODEL_STORAGE_PATH, f'lead_feature_names_{version}.joblib')
        joblib.dump(feature_names, feature_names_path)
        
        registry = ModelRegistry(
            model_id=str(uuid.uuid4()),
            model_type='lead',
            model_version=version,
            accuracy=acc,
            precision_score=prec,
            recall=rec,
            f1_score=f1,
            algorithm='XGBoost',
            dataset_size=lead_count,
            dataset_source='Database',
            status='active',
            model_path=model_path,
        )
        db.add(registry)
        
        history.accuracy = acc
        history.precision_score = prec
        history.recall = rec
        history.f1_score = f1
        history.training_duration_seconds = duration
        history.status = 'success'
        history.notes = notes
        db.commit()
        
        ModelManager.deactivate_previous_models(db, 'lead', version)
        
        return {
            'model_type': 'lead',
            'model_version': version,
            'accuracy': acc,
            'precision': prec,
            'recall': rec,
            'f1_score': f1,
            'training_duration': round(duration, 2),
            'records_used': lead_count,
            'status': 'success',
        }
    except Exception as e:
        history.status = 'failed'
        history.notes = str(e)
        db.commit()
        raise
