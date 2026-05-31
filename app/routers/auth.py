from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_db
from app.services.auth import register_user, authenticate_user
from app.schemas.user import UserCreate, UserResponse, UserLogin, Token
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse, status_code=201)
async def register(data: UserCreate, db = Depends(get_db)):
    try:
        result = await register_user(db, data)
    except ValueError as e:
        raise HTTPException(409, detail=str(e))

    return result

@router.post("/login", response_model=Token)
async def login(data: UserLogin, db = Depends(get_db)):
    try: 
        result = await authenticate_user(db, data)
        token = create_access_token({"sub": result.email})
    except ValueError as e:
        raise HTTPException(401, detail=str(e))
    
    return Token(access_token=token, token_type="bearer")