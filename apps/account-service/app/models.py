# app/models.py
from pydantic import BaseModel

class Account(BaseModel):
    account_id: str
    balance: float
    currency: str
