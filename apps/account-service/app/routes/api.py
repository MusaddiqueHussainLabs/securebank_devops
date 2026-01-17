# app/routes/api.py
from fastapi import APIRouter, Depends
from app.models import Account
from app.dependencies import get_current_user
from app.db.sample_users import accounts_db

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/", response_model=list[Account])
def list_accounts(user=Depends(get_current_user)):
    return accounts_db
