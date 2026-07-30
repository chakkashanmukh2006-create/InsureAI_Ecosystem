import time
from app.database.session import SessionLocal
from app.prediction.lead_predictor import LeadPredictor
from app.prediction.customer_predictor import CustomerPredictor

def main():
    db = SessionLocal()
    
    print("Testing LeadPredictor.get_top20...")
    lp = LeadPredictor()
    start = time.time()
    res = lp.get_top20(db)
    print(f"Count: {len(res)}, Time: {time.time() - start:.4f}s")
    
    print("Testing CustomerPredictor.get_high_risk...")
    cp = CustomerPredictor()
    start = time.time()
    res = cp.get_high_risk(db)
    print(f"Count: {len(res)}, Time: {time.time() - start:.4f}s")
    
    print("Testing LeadPredictor.get_all_predicted...")
    start = time.time()
    res = lp.get_all_predicted(db)
    print(f"Count: {len(res)}, Time: {time.time() - start:.4f}s")
    
    print("Testing CustomerPredictor.get_all_predicted...")
    start = time.time()
    res = cp.get_all_predicted(db)
    print(f"Count: {len(res)}, Time: {time.time() - start:.4f}s")

if __name__ == "__main__":
    main()
