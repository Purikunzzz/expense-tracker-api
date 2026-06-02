from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routers import auth, categories

app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(categories.router)


@app.get("/health")
async def health():
    return {"message": "expense tracker is running"}