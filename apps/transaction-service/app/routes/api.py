# app/routes/api.py
from fastapi import APIRouter, Depends
from app.models import Transaction
from app.dependencies import get_current_user
from app.db.sample_users import transactions_db

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=Transaction)
def create_transaction(
    tx: Transaction,
    user=Depends(get_current_user),
):
    transactions_db.append(tx.model_dump())
    return tx

@router.get("/")
def list_transactions(user=Depends(get_current_user)):
    return transactions_db
