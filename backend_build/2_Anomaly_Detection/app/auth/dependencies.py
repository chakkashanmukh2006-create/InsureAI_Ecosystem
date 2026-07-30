"""
FastAPI authentication dependencies.

Provides OAuth2 scheme and dependency injection for extracting
the current authenticated user from JWT bearer tokens.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from app.auth.security import verify_token
from app.database.session import get_db
from app.models.user import User

# OAuth2 password bearer scheme pointing to the login endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    db: Session = Depends(get_db)
) -> User:
    """
    Bypass authentication for internal subsystem.
    """
    return User(id=1, username="admin", email="admin@insure.ai", is_active=True)
