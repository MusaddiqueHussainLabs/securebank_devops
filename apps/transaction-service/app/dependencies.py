# app/dependencies.py
from typing import Annotated
from fastapi import Depends, Header
from app.security import verify_jwt

def get_current_user(
    authorization: Annotated[str, Header()],
):
    token = authorization.replace("Bearer ", "")
    return verify_jwt(token)
