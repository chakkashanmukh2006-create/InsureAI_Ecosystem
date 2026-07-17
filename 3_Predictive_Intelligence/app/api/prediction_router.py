from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.database.session import get_db
from app.models.training import ModelRegistry
from app.models.user import User
from app.auth.dependencies import get_current_user
from datetime import datetime, timedelta
import joblib
import pandas as pd
import numpy as np

try:
    from prophet import Prophet
    HAS_PROPHET = True
except ImportError:
    HAS_PROPHET = False
    from sklearn.linear_model import LinearRegression

router = APIRouter()


@router.get("/predictions/forecast", summary="Get Conversion Forecast", description="Get forecasted overall conversion volumes.")
def get_forecast(
    days: int = 30,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Load forecast model
    model_record = db.query(ModelRegistry).filter(
        ModelRegistry.model_type == 'forecast',
        ModelRegistry.status == 'active'
    ).order_by(desc(ModelRegistry.id)).first()

    if not model_record:
        raise HTTPException(status_code=404, detail="No active forecast model found.")

    model = joblib.load(model_record.model_path)
    
    future_dates = [datetime.now() + timedelta(days=i) for i in range(1, days + 1)]
    
    if HAS_PROPHET and isinstance(model, Prophet):
        future_df = pd.DataFrame({'ds': future_dates})
        # Remove tzinfo from ds column to match Prophet's expectations
        future_df['ds'] = future_df['ds'].dt.tz_localize(None)
        forecast = model.predict(future_df)
        predictions = [{"date": row['ds'].strftime('%Y-%m-%d'), "volume": max(0, int(row['yhat']))} for _, row in forecast.iterrows()]
    else:
        # Linear regression fallback
        future_df = pd.DataFrame({'ds': future_dates})
        future_df['ds_num'] = future_df['ds'].map(datetime.toordinal)
        y_pred = model.predict(future_df[['ds_num']])
        predictions = [{"date": d.strftime('%Y-%m-%d'), "volume": max(0, int(y))} for d, y in zip(future_dates, y_pred)]

    return {
        "model_version": model_record.model_version,
        "algorithm": model_record.algorithm,
        "forecast": predictions
    }
