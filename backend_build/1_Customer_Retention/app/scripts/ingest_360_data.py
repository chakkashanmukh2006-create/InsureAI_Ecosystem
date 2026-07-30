import os
import sys
import pandas as pd

# Add app to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.session import SessionLocal
from app.models.customer_360 import Customer360Profile, Customer360Policy

def ingest():
    db = SessionLocal()
    try:
        # Paths to datasets
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(base_dir)
        profiles_path = os.path.join(root_dir, "datasets", "customer_360_profiles.csv")
        policies_path = os.path.join(root_dir, "datasets", "customer_360_policies.csv")
        
        print("Reading profiles...")
        df_profiles = pd.read_csv(profiles_path)
        
        print("Clearing old 360 data...")
        db.query(Customer360Policy).delete()
        db.query(Customer360Profile).delete()
        db.commit()
        
        print("Ingesting profiles...")
        profiles = []
        for _, row in df_profiles.iterrows():
            profile = Customer360Profile(
                customer_id=row["customer_id"],
                name=row["name"],
                age=row["age"],
                city=row["city"],
                feedback_notes=row["feedback_notes"],
                sentiment_label=row["sentiment_label"]
            )
            profiles.append(profile)
        db.add_all(profiles)
        db.commit()
        
        print("Ingesting policies...")
        df_policies = pd.read_csv(policies_path)
        policies = []
        for _, row in df_policies.iterrows():
            policy = Customer360Policy(
                transaction_id=row["transaction_id"],
                customer_id=row["customer_id"],
                policy_type=row["policy_type"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                premium_amount=row["premium_amount"],
                status=row["status"],
                claim_history=row["claim_history"]
            )
            policies.append(policy)
        
        # Batch insert
        db.add_all(policies)
        db.commit()
        print("✅ 360 Data Ingestion Complete.")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    ingest()
