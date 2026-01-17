# app/models.py
from pydantic import BaseModel

class Notification(BaseModel):
    channel: str
    recipient: str
    message: str
