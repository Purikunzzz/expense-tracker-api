from fastapi import FastAPI
from app.routers import auth, categories, expenses, summary

app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(expenses.router)
app.include_router(summary.router)

@app.get("/health")
async def health():
    return {"message": "expense tracker is running"}