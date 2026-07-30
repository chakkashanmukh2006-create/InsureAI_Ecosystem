import time
from app.database.session import SessionLocal
from app.prediction.lead_predictor import LeadPredictor
from app.prediction.customer_predictor import CustomerPredictor

def main():
    db = SessionLocal()
    
    # Check predictions performance
    lp = LeadPredictor()
    cp = CustomerPredictor()

    print("Running Customer predict_all...")
    start = time.time()
    try:
        cp.predict_all(db)
    except Exception as e:
        print("Error:", e)
    print(f"Time: {time.time() - start:.4f}s")
    
    print("Running Lead predict_all...")
    start = time.time()
    try:
        lp.predict_all(db)
    except Exception as e:
        print("Error:", e)
    print(f"Time: {time.time() - start:.4f}s")

if __name__ == "__main__":
    main()
