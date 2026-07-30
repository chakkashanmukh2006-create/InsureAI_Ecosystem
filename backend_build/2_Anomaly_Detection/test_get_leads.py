import sys
from app.database.session import SessionLocal
from app.prediction.lead_predictor import LeadPredictor
from app.prediction.customer_predictor import CustomerPredictor

db = SessionLocal()
lp = LeadPredictor()
cp = CustomerPredictor()

print(f"Top 20 leads: {len(lp.get_top20(db))}")
print(f"High risk customers: {len(cp.get_high_risk(db))}")
print(f"All predicted leads: {len(lp.get_all_predicted(db))}")
print(f"All predicted customers: {len(cp.get_all_predicted(db))}")
