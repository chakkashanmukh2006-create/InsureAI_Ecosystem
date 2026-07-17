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
        return "CRITICAL: Call immediately and offer 10% discount"
    elif lead_score > 50:
        return "HIGH: Send personalized follow-up email"
    elif last_interaction_days > 14:
        return "MEDIUM: Add to re-engagement drip campaign"
    else:
        return "LOW: Continue standard nurturing process"

def generate_customer_dialogue(churn_ratio: float, support_tickets: int) -> str:
    if churn_ratio > 0.7 or support_tickets > 3:
        return "CRITICAL: Call immediately and offer a personalized retention package"
    elif churn_ratio > 0.4:
        return "HIGH: Send a proactive check-in email"
    else:
        return "LOW: Standard quarterly review call"

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
