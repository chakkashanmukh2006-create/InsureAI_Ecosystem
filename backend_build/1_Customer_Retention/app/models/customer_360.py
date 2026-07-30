"""
Customer 360 models for managing relational profile and policy history.
Designed to be non-destructive to the original flat Customer model.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base

class Customer360Profile(Base):
    """Core profile for the 360 view."""
    __tablename__ = "customer_360_profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    age = Column(Integer)
    city = Column(String(100))
    feedback_notes = Column(String, nullable=True)
    sentiment_label = Column(String(50), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    
    policies = relationship("Customer360Policy", back_populates="profile", cascade="all, delete-orphan")

class Customer360Policy(Base):
    """Transactional history tracking 5 years of multiple insurances."""
    __tablename__ = "customer_360_policies"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(String(50), unique=True, nullable=False, index=True)
    customer_id = Column(String(50), ForeignKey("customer_360_profiles.customer_id"), nullable=False, index=True)
    policy_type = Column(String(100), nullable=False)
    start_date = Column(String(20))
    end_date = Column(String(20))
    premium_amount = Column(Float, nullable=False)
    status = Column(String(50))  # Active, Expired, Cancelled
    claim_history = Column(Integer, default=0)
    
    profile = relationship("Customer360Profile", back_populates="policies")
