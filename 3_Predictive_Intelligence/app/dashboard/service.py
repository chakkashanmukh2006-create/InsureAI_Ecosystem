from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.lead import Lead
from app.models.customer import Customer
from app.models.call_logs import CallLog
from app.models.prediction import LeadPrediction, CustomerPrediction
from app.models.training import TrainingHistory, ModelRegistry
from app.schemas.dashboard import (
    DashboardResponse,
    DashboardStats,
    TrainingDashboardResponse,
    ModelDashboardResponse
)


class DashboardService:
    def get_dashboard(self, db: Session) -> DashboardResponse:
        total_leads = db.query(Lead).count()
        total_customers = db.query(Customer).count()
        total_calls = db.query(CallLog).count()
        total_lead_preds = db.query(LeadPrediction).count()
        total_cust_preds = db.query(CustomerPrediction).count()
        total_training = db.query(TrainingHistory).count()
        
        # Latest active models
        latest_forecast = db.query(ModelRegistry).filter(
            ModelRegistry.model_type == 'forecast', ModelRegistry.status == 'active'
        ).order_by(desc(ModelRegistry.id)).first()
        
        latest_lead = db.query(ModelRegistry).filter(
            ModelRegistry.model_type == 'lead', ModelRegistry.status == 'active'
        ).order_by(desc(ModelRegistry.id)).first()
        
        stats = DashboardStats(
            total_leads=total_leads,
            total_customers=total_customers,
            total_calls=total_calls,
            total_predictions_leads=total_lead_preds,
            total_predictions_customers=total_cust_preds,
            total_training_sessions=total_training,
            latest_lead_model_version=latest_forecast.model_version if latest_forecast else None,
            latest_customer_model_version=None,
            latest_lead_accuracy=latest_lead.accuracy if latest_lead else None,
            latest_customer_accuracy=None,
            latest_lead_precision=latest_lead.precision_score if latest_lead else None,
            latest_lead_recall=latest_lead.recall if latest_lead else None,
            latest_lead_f1_score=latest_lead.f1_score if latest_lead else None
        )
        
        recent = db.query(TrainingHistory).order_by(
            desc(TrainingHistory.training_datetime)
        ).limit(10).all()
        
        return DashboardResponse(stats=stats, recent_training=recent)
    
    def get_training_dashboard(self, db: Session) -> TrainingDashboardResponse:
        """Get the training history dashboard.
        
        Returns all training sessions ordered by most recent first.
        
        Args:
            db: Database session.
        
        Returns:
            TrainingDashboardResponse with full history and count.
        """
        history = db.query(TrainingHistory).order_by(
            desc(TrainingHistory.training_datetime)
        ).all()
        return TrainingDashboardResponse(
            training_history=history,
            total_sessions=len(history)
        )
    
    def get_model_dashboard(self, db: Session) -> ModelDashboardResponse:
        """Get the model registry dashboard.
        
        Returns all registered models ordered by most recent training date.
        
        Args:
            db: Database session.
        
        Returns:
            ModelDashboardResponse with all models and count.
        """
        models = db.query(ModelRegistry).order_by(
            desc(ModelRegistry.training_date)
        ).all()
        return ModelDashboardResponse(
            models=models,
            total_models=len(models)
        )
