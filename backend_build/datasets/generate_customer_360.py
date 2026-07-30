import pandas as pd
import numpy as np
import uuid
import random
from datetime import datetime, timedelta
import os

# Configuration
NUM_CUSTOMERS = 500
POLICY_TYPES = ["Health Insurance", "Life Insurance", "Motor Insurance", "Accidental Insurance"]
YEARS_HISTORY = 5
BASE_DATE = datetime(2026, 7, 1)

# NLP Feedback Dictionary
POSITIVE_FEEDBACK = [
    "I am very happy with the coverage and the easy claim process.",
    "The premium is affordable and the support team is excellent.",
    "Great experience so far. Highly recommend the health bundle.",
    "Quick responses. Thinking about upgrading my motor insurance.",
    "Very satisfied with the accidental coverage terms."
]
NEGATIVE_FEEDBACK = [
    "The premiums are too expensive and keep increasing every year.",
    "Terrible customer service. Waiting too long for claims.",
    "I am unhappy with the hidden fees in my life insurance policy.",
    "Thinking of cancelling. Found a cheaper motor insurance elsewhere.",
    "Very frustrating experience with the recent claim rejection."
]
NEUTRAL_FEEDBACK = [
    "Just renewing my standard policy for another year.",
    "No issues, everything is fine.",
    "I have some questions about the coverage limits, please call me.",
    "Standard service, nothing special to note.",
    "Need to update my address on the accidental policy."
]

def generate_360_datasets():
    profiles = []
    policies = []
    
    print("Generating Customer 360 Dataset...")
    
    for i in range(NUM_CUSTOMERS):
        cust_id = f"C360-100{i:03d}"
        name = f"User {random.randint(1, 9999)}"
        age = random.randint(25, 65)
        city = random.choice(["New York", "London", "Sydney", "Toronto", "Berlin"])
        
        # Determine sentiment & feedback
        sentiment_roll = random.random()
        if sentiment_roll > 0.7:
            feedback = random.choice(POSITIVE_FEEDBACK)
            sentiment_label = "Positive"
        elif sentiment_roll > 0.4:
            feedback = random.choice(NEUTRAL_FEEDBACK)
            sentiment_label = "Neutral"
        else:
            feedback = random.choice(NEGATIVE_FEEDBACK)
            sentiment_label = "Negative"
            
        profiles.append({
            "customer_id": cust_id,
            "name": name,
            "age": age,
            "city": city,
            "feedback_notes": feedback,
            "sentiment_label": sentiment_label
        })
        
        # Determine customer engagement level
        # highly engaged customers get all 4 policies for 5 years (20 records)
        engagement_level = random.choice(["High", "Medium", "Low"])
        
        active_policy_types = []
        if engagement_level == "High":
            active_policy_types = POLICY_TYPES # all 4
        elif engagement_level == "Medium":
            active_policy_types = random.sample(POLICY_TYPES, 2)
        else:
            active_policy_types = random.sample(POLICY_TYPES, 1)
            
        # Generate transactional records
        for p_type in active_policy_types:
            # Randomize premium amount base
            base_premium = random.randint(300, 1500)
            
            # Create a 5-year transactional history for this policy type
            for year in range(YEARS_HISTORY):
                start_date = BASE_DATE - timedelta(days=365 * (YEARS_HISTORY - year))
                end_date = start_date + timedelta(days=365)
                
                # If it's the current year, it's active. Past years are expired.
                status = "Active" if year == (YEARS_HISTORY - 1) else "Expired"
                
                # Simulate churn for some "Negative" customers (stop renewing)
                if sentiment_label == "Negative" and year == (YEARS_HISTORY - 1) and random.random() > 0.5:
                    status = "Cancelled"
                if sentiment_label == "Negative" and year < (YEARS_HISTORY - 1) and random.random() > 0.8:
                    break # Stop creating history, they churned early
                    
                # Adjust premium slightly per year
                premium = base_premium + (year * random.randint(10, 50))
                
                policies.append({
                    "transaction_id": f"TXN-{uuid.uuid4().hex[:8]}",
                    "customer_id": cust_id,
                    "policy_type": p_type,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date.strftime("%Y-%m-%d"),
                    "premium_amount": premium,
                    "status": status,
                    "claim_history": random.choices([0, 1, 2], weights=[0.8, 0.15, 0.05])[0]
                })

    df_profiles = pd.DataFrame(profiles)
    df_policies = pd.DataFrame(policies)
    
    # Save to root datasets folder for easy upload testing
    df_profiles.to_csv("customer_360_profiles.csv", index=False)
    df_policies.to_csv("customer_360_policies.csv", index=False)
    
    print(f"✅ Generated {len(df_profiles)} 360 profiles.")
    print(f"✅ Generated {len(df_policies)} transactional policy records.")
    
if __name__ == "__main__":
    generate_360_datasets()
