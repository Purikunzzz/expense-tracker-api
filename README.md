## About The Project
- Personal expense tracking REST API with monthly analytics, 
built with FastAPI & PostgreSQL, featuring JWT authentication.

## User
- People who want to know and improve their own spending by monthly review and summary dashboard

## Stack

### Web framework
- fastapi==0.111.0
- uvicorn[standard]==0.29.0

### Database
- sqlalchemy==2.0.30
- asyncpg==0.29.0
- alembic==1.13.1          # DB migrations

### Validation & settings
- pydantic==2.7.1
- pydantic-settings==2.2.1

### Auth
- python-jose[cryptography]==3.3.0   # JWT
- passlib[bcrypt]==1.7.4             # Password hashing

### Utilities
- python-multipart==0.0.9  # For form data (login form support)
- python-dotenv==1.0.1


## Architecture
```
expense-tracker/
├── app/
│   ├── core/          # config, database, security
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   ├── routers/       # HTTP endpoints
│   ├── services/      # Business logic
│   ├── dependencies.py
│   └── main.py
├── alembic/
│   └── versions/      # Database migrations
├── .env               # Environment variables (not committed)
├── requirements.txt
└── build.sh           # Render build script
```


## API Endpoints

### auth
- POST /auth/register
- POST /auth/login
- GET  /auth/me

### categories
- GET    /categories
- POST   /categories
- GET    /categories/{categories_id}
- PATCH  /categories/{categories_id}
- DELETE /categories/{categories_id}

### expenses
- GET    /expenses
- POST   /expenses
- GET    /expenses/{expenses_id}
- PATCH  /expenses/{expenses_id}
- DELETE /expenses/{expenses_id}

### summary
- GET /summary

### default
- GET /health

## Setup
1. Clone repo
2. Create .env file (see .env.example)
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `alembic upgrade head`
5. Start server: `uvicorn app.main:app --reload`

## Live URL
- https://expense-tracker-api-64u9.onrender.com

## Related
- Frontend: https://expense-tracker-frontend-pink-one.vercel.app
- API Docs: https://expense-tracker-api-64u9.onrender.com/docs

