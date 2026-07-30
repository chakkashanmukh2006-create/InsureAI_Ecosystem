"""
Call Log schemas.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CallLogBase(BaseModel):
    agent_id: str
    call_duration: float
    outcome: str
    call_date: Optional[datetime] = None


class CallLogCreate(CallLogBase):
    pass


class CallLogResponse(CallLogBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
