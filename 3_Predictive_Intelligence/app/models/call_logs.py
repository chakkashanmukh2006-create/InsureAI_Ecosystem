"""
Call Logs model.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class CallLog(Base):
    """Call Log model representing call details."""

    __tablename__ = "call_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(String(50), nullable=False, index=True)
    call_duration = Column(Float, nullable=False)
    outcome = Column(String(100), nullable=False)
    call_date = Column(DateTime, nullable=False, default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return f"<CallLog(id={self.id}, agent_id='{self.agent_id}', outcome='{self.outcome}')>"
