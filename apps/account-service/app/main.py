# app/main.py
from fastapi import FastAPI
from app.routes.api import router

app = FastAPI(title="Account Service")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "account-service healthy"}
