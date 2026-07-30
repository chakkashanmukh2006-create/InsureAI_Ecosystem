import sys
import logging
from app.database.session import SessionLocal
from app.prediction.lead_predictor import LeadPredictor
from app.prediction.customer_predictor import CustomerPredictor

logging.basicConfig(level=logging.INFO)

db = SessionLocal()

print("Running Lead predict_all...")
try:
    lp = LeadPredictor()
    lp.predict_all(db)
    print(f"Generated {len(lp.get_top20(db))} top leads.")
except Exception as e:
    print(f"Lead Predictor failed: {e}")

print("Running Customer predict_all...")
try:
    cp = CustomerPredictor()
    cp.predict_all(db)
    print(f"Generated {len(cp.get_high_risk(db))} high risk customers.")
except Exception as e:
    print(f"Customer Predictor failed: {e}")
