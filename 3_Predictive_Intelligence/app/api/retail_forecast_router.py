from fastapi import APIRouter, Query
import pandas as pd
import numpy as np
import os
from datetime import timedelta

# Models
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX
from prophet import Prophet
import xgboost as xgb
import warnings
warnings.filterwarnings("ignore")

router = APIRouter()

def get_kaggle_dataset():
    csv_path = os.path.join(os.path.dirname(__file__), "../../../datasets/kaggle_real_superstore.csv")
    df = pd.read_csv(csv_path)
    # The Kaggle Superstore dates are typically "DD/MM/YYYY" or "M/D/YY"
    df['Order Date'] = pd.to_datetime(df['Order Date'], format="mixed", dayfirst=False)
    return df

@router.get("/retail/options")
def get_retail_options():
    df = get_kaggle_dataset()
    categories = sorted(df['Category'].dropna().unique().tolist())
    products = sorted(df['Product Name'].dropna().unique().tolist())
    return {
        "categories": categories,
        "products": products
    }

@router.get("/retail/forecast")
def get_retail_forecast(
    level: str = Query("store", description="store, category, or product"),
    name: str = Query(None, description="The specific category or product name")
):
    """
    Load Real Kaggle Superstore dataset and run 5 different time series forecasting models.
    Supports Store, Category, and Product levels.
    """
    df = get_kaggle_dataset()
    
    if level == "category" and name:
        df = df[df['Category'] == name]
    elif level == "product" and name:
        df = df[df['Product Name'] == name]
    
    # Aggregate sales
    # If store level, we can do daily or weekly. Let's do weekly to smooth out noise for all levels.
    df_agg = df.groupby('Order Date')['Sales'].sum().reset_index()
    df_agg = df_agg.sort_values('Order Date')
    
    # Resample to weekly (W-MON) to make charts clean and predictable
    df_agg.set_index('Order Date', inplace=True)
    df_agg = df_agg.resample('W-MON').sum().reset_index()
    
    # We will forecast 12 weeks into the future
    HORIZON = 12
    
    if len(df_agg) < 15:
        # Not enough data
        return {"error": "Not enough historical data to forecast this item."}
    
    # Historical data for chart
    df_train = df_agg.copy()
    df_chart = df_train.tail(52).copy() # Last 52 weeks
    
    historical_dates = df_chart['Order Date'].dt.strftime('%Y-%m-%d').tolist()
    historical_values = df_chart['Sales'].tolist()
    
    future_dates_dt = [df_train['Order Date'].iloc[-1] + timedelta(weeks=i) for i in range(1, HORIZON + 1)]
    future_dates = [d.strftime('%Y-%m-%d') for d in future_dates_dt]
    
    series = df_train['Sales'].values
    
    # 1. Simple Moving Average (SMA)
    sma_value = np.mean(series[-4:]) # 4-week moving average
    sma_pred = [sma_value] * HORIZON
    
    # 2. Holt-Winters Exponential Smoothing
    try:
        hw_model = ExponentialSmoothing(series, seasonal_periods=52, trend='add', seasonal='add', initialization_method="estimated")
        hw_fit = hw_model.fit()
        hw_pred = hw_fit.forecast(HORIZON).tolist()
    except:
        # Fallback if seasonal periods fail
        hw_model = ExponentialSmoothing(series, trend='add', initialization_method="estimated")
        hw_fit = hw_model.fit()
        hw_pred = hw_fit.forecast(HORIZON).tolist()
    
    # 3. SARIMA
    try:
        sarima_model = SARIMAX(series, order=(1,1,1), seasonal_order=(0,0,0,0), enforce_stationarity=False, enforce_invertibility=False)
        sarima_fit = sarima_model.fit(disp=False)
        sarima_pred = sarima_fit.forecast(HORIZON).tolist()
    except:
        sarima_pred = [sma_value] * HORIZON
        
    # 4. Prophet
    prophet_df = df_train[['Order Date', 'Sales']].rename(columns={'Order Date': 'ds', 'Sales': 'y'})
    m = Prophet(weekly_seasonality=False, yearly_seasonality=True, daily_seasonality=False)
    m.fit(prophet_df)
    future = m.make_future_dataframe(periods=HORIZON, freq='W')
    prophet_forecast = m.predict(future)
    prophet_pred = prophet_forecast['yhat'].tail(HORIZON).tolist()
    
    # 5. XGBoost (Lag Features)
    xgb_df = df_train.copy()
    for lag in range(1, 5):
        xgb_df[f'lag_{lag}'] = xgb_df['Sales'].shift(lag)
    xgb_df['month'] = xgb_df['Order Date'].dt.month
    xgb_df = xgb_df.dropna()
    
    X_train = xgb_df[[f'lag_{lag}' for lag in range(1, 5)] + ['month']]
    y_train = xgb_df['Sales']
    
    xgb_model = xgb.XGBRegressor(n_estimators=50, max_depth=3)
    if len(X_train) > 5:
        xgb_model.fit(X_train, y_train)
        
        xgb_pred = []
        current_lags = y_train.tail(4).values[::-1].tolist()
        current_date = df_train['Order Date'].iloc[-1]
        
        for i in range(HORIZON):
            current_date += timedelta(weeks=1)
            X_test = pd.DataFrame([current_lags + [current_date.month]], columns=X_train.columns)
            pred = xgb_model.predict(X_test)[0]
            xgb_pred.append(float(pred))
            
            current_lags.insert(0, pred)
            current_lags.pop()
    else:
        xgb_pred = [sma_value] * HORIZON
        
    return {
        "dates": historical_dates + future_dates,
        "history": historical_values + [None] * HORIZON,
        "predictions": {
            "SMA": [None] * len(historical_values) + sma_pred,
            "HoltWinters": [None] * len(historical_values) + hw_pred,
            "SARIMA": [None] * len(historical_values) + sarima_pred,
            "Prophet": [None] * len(historical_values) + prophet_pred,
            "XGBoost": [None] * len(historical_values) + xgb_pred,
        }
    }
