import sys
from app.database.session import SessionLocal
from app.prediction.lead_predictor import LeadPredictor

db = SessionLocal()
lp = LeadPredictor()
res = lp.get_top20(db)
print(res[0])
