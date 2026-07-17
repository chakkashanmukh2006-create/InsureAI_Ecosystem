from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.database.session import get_db
from app.models.call_logs import CallLog
from app.models.user import User
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.get("/call-logs", summary="Get Recent Call Logs")
def get_call_logs(
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logs = db.query(CallLog).order_by(desc(CallLog.call_date)).limit(limit).all()
    return logs
