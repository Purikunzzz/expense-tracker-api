from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0"
)

app.include_router(auth.router)

@app.get("/health")
async def health():
    return {"message": "expense tracker is running"}