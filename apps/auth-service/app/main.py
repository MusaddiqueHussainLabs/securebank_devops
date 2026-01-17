# app/main.py
from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI(title="SecureBank Auth Service")

app.include_router(auth_router)

@app.get("/health")
def health():
    return {"status": "auth-service healthy"}
