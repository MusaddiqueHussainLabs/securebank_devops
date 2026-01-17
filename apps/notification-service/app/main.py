# app/main.py
from fastapi import FastAPI
from app.routes.api import router

app = FastAPI(title="Notification Service")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "notification-service healthy"}
