import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_retail_sales():
    print("Generating Kaggle-style Retail Demand Forecasting Dataset...")
    
    # 3 years of daily data
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * 3)
    
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Base daily sales
    base_sales = 5000
    
    # Trend: general upward growth over 3 years
    trend = np.linspace(0, 1500, len(dates))
    
    # Seasonality (Weekly) - Spikes on weekends
    weekly_seasonality = np.array([300 if d.weekday() >= 5 else 0 for d in dates])
    
    # Seasonality (Yearly) - Spikes in Nov/Dec for holiday shopping
    yearly_seasonality = np.array([
        800 if d.month == 11 else
        1500 if d.month == 12 else
        -200 if d.month == 1 else # Post holiday drop
        0 for d in dates
    ])
    
    # Random Noise
    noise = np.random.normal(0, 200, len(dates))
    
    # Combine components
    total_sales = base_sales + trend + weekly_seasonality + yearly_seasonality + noise
    # Ensure no negative sales
    total_sales = np.maximum(total_sales, 0)
    
    df = pd.DataFrame({
        'date': dates,
        'retail_sales': total_sales.astype(int)
    })
    
    # Save
    out_path = os.path.join(os.path.dirname(__file__), 'kaggle_retail_sales.csv')
    df.to_csv(out_path, index=False)
    print(f"✅ Generated {len(df)} rows of retail sales data at {out_path}")

if __name__ == "__main__":
    generate_retail_sales()
