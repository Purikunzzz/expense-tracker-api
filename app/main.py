from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routers import auth, categories, expenses, summary
from contextlib import asynccontextmanager
from alembic.config import Config
from alembic import command
import asyncio

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, run_migrations)
    yield



app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(expenses.router)
app.include_router(summary.router)


@app.get("/health")
async def health():
    return {"message": "expense tracker is running"}