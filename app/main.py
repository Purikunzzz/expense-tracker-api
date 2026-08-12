from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import auth, category, expense, summary
from alembic.config import Config
from alembic import command
import asyncio

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await asyncio.to_thread(run_migrations)
    yield

app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(auth.router)
app.include_router(category.router)
app.include_router(expense.router)
app.include_router(summary.router)

@app.get("/health")
async def health():
    return {"message": "expense tracker is running"}