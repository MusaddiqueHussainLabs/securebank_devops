# app/security.py
import jwt
from fastapi import HTTPException, status
from app.config import SECRET_KEY, ALGORITHM

def verify_jwt(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
