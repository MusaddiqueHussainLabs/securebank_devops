# app/routes/api.py
from fastapi import APIRouter
from app.models import Notification

router = APIRouter(prefix="/notify", tags=["Notifications"])

@router.post("/")
def send_notification(data: Notification):
    return {
        "status": "SENT",
        "channel": data.channel,
        "recipient": data.recipient,
        "message": data.message,
    }
