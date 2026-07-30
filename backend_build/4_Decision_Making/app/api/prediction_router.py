from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.lead import Lead
from app.models.customer import Customer
from app.models.prediction import LeadPrediction, CustomerPrediction
from app.models.user import User
from app.schemas.lead import LeadPredictionResponse
from app.schemas.customer import CustomerPredictionResponse
from app.auth.dependencies import get_current_user

router = APIRouter()

def generate_lead_dialogue(lead_score: float, last_interaction_days: int) -> str:
    if lead_score > 70 and last_interaction_days < 7:
        return "1. ACKNOWLEDGE: 'Hello! I noticed you were exploring our premium policies recently.'<br>2. VALUE PITCH: 'We have a limited-time 10% discount on comprehensive bundles.'<br>3. DISCOVERY: 'What specific coverage are you looking to secure today?'<br>4. OVERCOME OBJECTION: 'We require zero initial setup fees to get you started.'<br>5. CLOSING: 'Can I generate that discounted quote for you right now?'"
    elif lead_score > 50:
        return "1. GREETING: 'Hi! Just following up on your recent interest in Insure AI.'<br>2. NURTURE: 'We have some great resources comparing our coverage plans.'<br>3. VALUE ADD: 'I can send you a personalized comparison chart.'<br>4. NEXT STEP: 'Would you like to schedule a 5-minute consultation?'<br>5. CLOSING: 'I will shoot you an email right now with the details.'"
    elif last_interaction_days > 14:
        return "1. RE-ENGAGE: 'Hello, we haven't connected in a while regarding your quote.'<br>2. UPDATE: 'We have recently updated our policy offerings with better rates.'<br>3. INQUIRY: 'Are you still in the market for insurance coverage?'<br>4. VALUE ADD: 'I can quickly recalculate your quote with our new pricing model.'<br>5. CLOSING: 'Let me know if you would like to review the updated numbers.'"
    else:
        return "1. GREETING: 'Hello, this is Insure AI checking in on your profile.'<br>2. ASSISTANCE: 'Did you need any help navigating our policy options?'<br>3. NURTURE: 'Our team is here if you have any questions about coverage limits.'<br>4. RESOURCES: 'I recommend checking our FAQ page for quick answers.'<br>5. CLOSING: 'Feel free to reach out whenever you are ready.'"

def generate_customer_dialogue(churn_ratio: float, support_tickets: int) -> str:
    if churn_ratio > 0.7 or support_tickets > 3:
        return "1. EMPATHY: 'I am calling to personally address the recent issues on your account.'<br>2. ESCALATION: 'I have moved your tickets to our priority queue.'<br>3. VALUE ADD: 'You are a valued client and your satisfaction is critical.'<br>4. OFFER: 'I am authorizing a proactive 15% retention credit to your account.'<br>5. CLOSING: 'Can I apply this credit and resolve your tickets today?'"
    elif churn_ratio > 0.4:
        return "1. CHECK-IN: 'Hello! Calling for a proactive mid-year review.'<br>2. SATISFACTION: 'How has your experience been with our recent policy changes?'<br>3. DISCOVERY: 'Is there anything we can optimize regarding your premiums?'<br>4. VALUE ADD: 'I can run an audit to see if you qualify for any new discounts.'<br>5. CLOSING: 'I will follow up next week with the audit results.'"
    else:
        return "1. REVIEW: 'Hello, calling for your standard quarterly account review.'<br>2. VALIDATION: 'Everything looks perfect and your premiums are locked in.'<br>3. QUESTIONS: 'Have there been any major life changes we should know about?'<br>4. APPRECIATION: 'Thank you for your continued loyalty with Insure AI.'<br>5. CLOSING: 'We are always here if you need us in the future.'"

@router.get("/predictions/lead/{lead_id}", response_model=LeadPredictionResponse,
            summary="Get Lead Prediction",
            description="Get the latest prediction for a specific lead with full metadata.")
def get_lead_prediction(
    lead_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get the latest propensity prediction for a specific lead.
    
    Returns the most recent prediction including propensity score, category,
    top contributing reasons, and model metadata.
    
    Args:
        lead_id: The unique identifier for the lead.
    
    Raises:
        HTTPException: 404 if no prediction exists for the given lead.
    """
    # Get latest prediction for this lead
    prediction = db.query(LeadPrediction).filter(
        LeadPrediction.lead_id == lead_id
    ).order_by(LeadPrediction.prediction_timestamp.desc()).first()
    
    if not prediction:
        raise HTTPException(status_code=404, detail=f"No prediction found for lead {lead_id}")
    
    lead = db.query(Lead).filter(Lead.lead_id == lead_id).first()
    
    return LeadPredictionResponse(
        prediction_id=prediction.prediction_id,
        lead_id=prediction.lead_id,
        full_name=lead.full_name if lead else 'Unknown',
        propensity_ratio=prediction.propensity_ratio,
        lead_score=prediction.lead_score,
        category=prediction.category,
        top_reasons=prediction.top_reasons or [],
        email=prediction.email,
        contact_number=prediction.contact_number,
        model_version=prediction.model_version,
        model_accuracy=prediction.model_accuracy,
        algorithm=prediction.algorithm,
        prediction_timestamp=prediction.prediction_timestamp,
        training_timestamp=prediction.training_timestamp,
        dialogue_prompt=generate_lead_dialogue(
            prediction.lead_score, 
            lead.last_interaction_days if lead and lead.last_interaction_days is not None else 0
        )
    )


@router.get("/predictions/customer/{customer_id}", response_model=CustomerPredictionResponse,
            summary="Get Customer Prediction",
            description="Get the latest churn prediction for a specific customer.")
def get_customer_prediction(
    customer_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get the latest churn prediction for a specific customer.
    
    Returns the most recent prediction including churn probability, risk category,
    sentiment analysis, top contributing reasons, and model metadata.
    
    Args:
        customer_id: The unique identifier for the customer.
    
    Raises:
        HTTPException: 404 if no prediction exists for the given customer.
    """
    prediction = db.query(CustomerPrediction).filter(
        CustomerPrediction.customer_id == customer_id
    ).order_by(CustomerPrediction.prediction_timestamp.desc()).first()
    
    if not prediction:
        raise HTTPException(status_code=404, detail=f"No prediction found for customer {customer_id}")
    
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    
    return CustomerPredictionResponse(
        prediction_id=prediction.prediction_id,
        customer_id=prediction.customer_id,
        name=customer.name if customer else 'Unknown',
        churn_ratio=prediction.churn_ratio,
        risk_category=prediction.risk_category,
        sentiment=prediction.sentiment or 'Neutral',
        sentiment_score=prediction.sentiment_score or 0.0,
        confidence_score=prediction.confidence_score or 0.0,
        top_reasons=prediction.top_reasons or [],
        email=prediction.email,
        contact_number=prediction.contact_number,
        model_version=prediction.model_version,
        model_accuracy=prediction.model_accuracy,
        algorithm=prediction.algorithm,
        prediction_timestamp=prediction.prediction_timestamp,
        training_timestamp=prediction.training_timestamp,
        dialogue_prompt=generate_customer_dialogue(
            prediction.churn_ratio,
            customer.support_tickets if customer and customer.support_tickets is not None else 0
        )
    )
