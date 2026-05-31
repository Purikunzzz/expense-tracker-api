from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.security import hash_password, verify_password


async def register_user(db: AsyncSession, data: UserCreate) -> User:
    result = await db.execute(select(User).where(User.email == data.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise ValueError("Email Already exists")

    new_user = User(
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def authenticate_user(db: AsyncSession, data: UserLogin):
    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()
    
    if not user:
        raise ValueError("Email or password is incorrect")

    if not verify_password(data.password, user.hashed_password):
        raise ValueError("Email or password is incorrect")

    return user




