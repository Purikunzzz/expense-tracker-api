from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category
from app.schemas.categories import CategoryCreate, CategoryResponse, CategoryUpdate

async def create_category(db: AsyncSession, user_id: int, data: CategoryCreate) -> Category:
    category = Category(
        name=data.name,
        description=data.description,
        user_id=user_id,
    )
    db.add(category)
    await db.commit()
    await db.refresh(category)

    return category

async def get_categories(db: AsyncSession, user_id: int) -> list[Category]:
    result = await db.execute(select(Category).where(Category.user_id == user_id))
    return list(result.scalars().all())

async def get_category(db: AsyncSession, user_id: int, category_id: int) -> Category | None:
    result = await db.execute(select(Category).where(Category.id == category_id, Category.user_id == user_id))
    return result.scalar_one_or_none()

async def update_category(db: AsyncSession, user_id: int, category_id: int, data: CategoryUpdate) -> Category:
    category = await get_category(db, user_id, category_id)
    if not category:
        raise ValueError(f"user_id:{user_id}, category_id:{category_id} is not found")
    
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)
    
    await db.commit()
    await db.refresh(category)
    return category

async def delete_category(db: AsyncSession, user_id: int, category_id: int) -> None:
    category = await get_category(db, user_id, category_id)
    if not category:
        raise ValueError(f"user_id:{user_id}, category_id:{category_id} is not found")
    
    await db.delete(category)
    await db.commit()