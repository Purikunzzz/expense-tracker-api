from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user
from app.schemas.categories import CategoryCreate, CategoryResponse, CategoryUpdate
from app.services.category import create_category, get_categories, get_category, delete_category, update_category

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=list[CategoryResponse], status_code=200)
async def get_all_categories(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    return await get_categories(db, current_user.id)

@router.get("/{category_id}", response_model=CategoryResponse, status_code=200)
async def get_category_by_id(category_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    
    try:
        category = await get_category(db, category_id, current_user.id)
        if not category:
            raise HTTPException(status_code=404, detail="category not found")
        return category
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=CategoryResponse, status_code=201)
async def create_new_category(body: CategoryCreate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return await create_category(db, current_user.id, body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{category_id}", response_model=CategoryResponse, status_code=200)
async def update_category_by_id(category_id: int, body: CategoryUpdate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return await update_category(db, current_user.id, category_id, body)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{category_id}", status_code=204)
async def delete_category_by_id(category_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return await delete_category(db, current_user.id, category_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    



