from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, categories, expenses, summary

app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://expense-tracker-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(expenses.router)
app.include_router(summary.router)

@app.get("/health")
async def health():
    return {"message": "expense tracker is running"}