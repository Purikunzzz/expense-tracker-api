# CLAUDE.md — Personal Expense Tracker

## Project overview
A RESTful API for tracking personal expenses, built with FastAPI.
Users can register, log in, manage expenses with categories, and view monthly summaries.

## Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy (async preferred)
- **Database**: PostgreSQL
- **Validation**: Pydantic v2
- **Auth**: JWT (python-jose + passlib)
- **Python**: 3.11+

## Project structure
```
expense-tracker/
├── app/
│   ├── main.py           # FastAPI app factory, router registration
│   ├── dependencies.py   # Shared FastAPI dependencies (get_db, get_current_user)
│   ├── models/           # SQLAlchemy ORM models
│   ├── schemas/          # Pydantic request/response schemas
│   ├── routers/          # Route handlers (thin layer — call services)
│   ├── services/         # Business logic (no direct HTTP knowledge)
│   └── core/
│       ├── config.py     # Settings via pydantic-settings
│       ├── security.py   # Password hashing, JWT creation/verification
│       └── database.py   # Engine, session factory
├── .env                  # Secrets (never commit)
├── requirements.txt
└── CLAUDE.md
```

## Architecture rules
- Routers handle HTTP concerns only (request parsing, response codes).
- Business logic lives in services/. Routers call services; services do the work.
- Models are SQLAlchemy only. Schemas are Pydantic only. Never mix them.
- Dependencies (get_db, get_current_user) are injected — never called directly inside handlers.

## Naming conventions
- Files and folders: `snake_case`
- SQLAlchemy models: `PascalCase` class names (e.g. `Expense`, `Category`)
- Pydantic schemas: `PascalCase` + suffix (e.g. `ExpenseCreate`, `ExpenseResponse`)
- Router prefix pattern: `/api/v1/<resource>`

## Environment variables (required in .env)
```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/expense_tracker
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Auth flow
- Register: `POST /api/v1/auth/register`
- Login: `POST /api/v1/auth/login` → returns `{ access_token, token_type }`
- Protected routes: `Authorization: Bearer <token>` header required


## Key dependencies
See `requirements.txt`. Install with:
```bash
pip install -r requirements.txt
```

## Notes for Claude
- Guide, don't write full code. Ask what the user thinks before giving answers.
- Point out what's good and what to improve in code reviews.
- When explaining concepts, ask a follow-up question to check understanding.