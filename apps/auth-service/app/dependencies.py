# app/dependencies.py
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.models import User, UserInDB, TokenData
from app.security import decode_token
from app.db.sample_users import sample_users_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db, username: str):
    if username in db:
        return UserInDB(**db[username])

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    payload = decode_token(token)
    username: str | None = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    user = get_user(sample_users_db, username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
