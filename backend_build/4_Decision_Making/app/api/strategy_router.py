from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class PolicyInput(BaseModel):
    policy_type: str
    status: str

class StrategyRequest(BaseModel):
    customer_id: str
    sentiment_score: float
    churn_risk_percent: float
    propensity_percent: float
    behavioral_keywords: List[str]
    policies: List[PolicyInput]

class StrategyResponse(BaseModel):
    customer_id: str
    primary_objective: str
    workflow_steps: List[str]

@router.post("/prescriptive_workflow", response_model=StrategyResponse)
def generate_prescriptive_workflow(request: StrategyRequest):
    """
    Generates a 5-step prescriptive strategy for a Customer 360 profile.
    Analyzes active/inactive policies and NLP sentiment to recommend cross-sells or retention strategies.
    """
    active_policies = [p.policy_type for p in request.policies if p.status == "Active"]
    
    steps = []
    objective = "Retention"
    
    # Analyze Cross-sell opportunities
    has_motor = "Motor Insurance" in active_policies
    has_health = "Health Insurance" in active_policies
    has_life = "Life Insurance" in active_policies
    has_accidental = "Accidental Insurance" in active_policies
    
    if request.churn_risk_percent > 70:
        objective = "High-Risk Retention Intervention (Dialogue Script)"
        steps.append('1. ACKNOWLEDGE: "I reviewed your recent feedback and I want to immediately address the specific frustrations you experienced."')
        steps.append('2. RESOLUTION: "I have personally escalated your previous claim ticket to our senior resolution team for priority processing."')
        steps.append('3. VALUE REINFORCEMENT: "We highly value your 5-year history with us, which is why we are assigning a dedicated case manager to your account."')
        steps.append('4. FINANCIAL OFFER: "To demonstrate our commitment, I am authorized to apply a 15% loyalty retention discount to your upcoming premium."')
        steps.append('5. CLOSING: "Can I go ahead and apply that discount to your account and finalize the escalation today?"')
        
    elif request.propensity_percent > 70:
        objective = "Strategic Upsell / Cross-Sell (Dialogue Script)"
        if has_motor and not has_health:
            steps.append('1. ACKNOWLEDGE: "I am reviewing your excellent driving record and positive history on your Motor Insurance policy."')
            steps.append('2. TRANSITION: "Because of your preferred status, you qualify for our exclusive multi-policy health bundle this month."')
            steps.append('3. STRATEGIC PITCH: "Adding Health Insurance to your portfolio will actually trigger a 10% reduction on your overall premium costs."')
            steps.append('4. VALUE ADD: "You receive full medical coverage for a fraction of the standard rate by utilizing your bundled discount."')
            steps.append('5. CLOSING: "I have a pre-approved quote ready for you right now—shall we run through the numbers?"')
        elif has_health and not has_life:
            steps.append('1. ACKNOWLEDGE: "I am reviewing your current Health Insurance benefits and the comprehensive coverage you have secured."')
            steps.append('2. TRANSITION: "While your medical coverage is solid, our predictive analysis suggests a potential gap in long-term family protection."')
            steps.append('3. STRATEGIC PITCH: "Pairing your health policy with our Term Life Insurance ensures total financial security for your dependents."')
            steps.append('4. VALUE ADD: "By bundling them today, we waive all underwriting fees and lock in a permanent premium rate."')
            steps.append('5. CLOSING: "Can I take two minutes to show you the financial breakdown of adding Life Insurance to your plan?"')
        else:
            steps.append('1. ACKNOWLEDGE: "Thank you for maintaining a comprehensive insurance portfolio with Insure AI across multiple product lines."')
            steps.append('2. TRANSITION: "Based on your high engagement score, you are eligible for our Premium Diamond Upgrade."')
            steps.append('3. STRATEGIC PITCH: "This upgrade increases all your policy limits by 50% while lowering your cross-policy deductibles to zero."')
            steps.append('4. VALUE ADD: "This provides ultimate financial protection and VIP claims processing across all your active policies."')
            steps.append('5. CLOSING: "Would you like me to activate the Premium Diamond upgrade for your portfolio today?"')
            
    else:
        objective = "Standard Relationship Maintenance (Dialogue Script)"
        steps.append('1. ACCOUNT REVIEW: "I am calling to conduct your annual portfolio review to ensure your coverages match your current risk profile."')
        steps.append('2. COVERAGE CHECK: "We need to verify if there have been any major asset acquisitions or lifestyle changes in the past year."')
        steps.append('3. RENEWAL STRATEGY: "Your auto-renewal is coming up next month and your current premium rates have been successfully locked in."')
        steps.append('4. OPTIMIZATION: "Are there any specific coverages you feel are lacking, or areas where we can reduce your exposure?"')
        steps.append('5. CLOSING: "I will document this review in your file. Please reach out immediately if your risk profile changes."')
        
    # Ensure exactly 5 steps
    while len(steps) < 5:
        steps.append(f"{len(steps)+1}. General account maintenance and monitoring.")
        
    return StrategyResponse(
        customer_id=request.customer_id,
        primary_objective=objective,
        workflow_steps=steps[:5]
    )
