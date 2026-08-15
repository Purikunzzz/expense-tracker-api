from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user
from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate
from app.services.expense import get_expense, get_expenses, create_expense, update_expense, delete_expense

router = APIRouter(prefix="/expenses", tags=["expense"])

@router.get("/", response_model=list[ExpenseResponse], status_code=200)
async def get_all_expenses(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    return await get_expenses(db, current_user.id)

@router.get("/{expense_id}", response_model=ExpenseResponse, status_code=200)
async def get_expense_by_id(expense_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        expense =  await get_expense(db, current_user.id, expense_id)
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        return expense
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=ExpenseResponse, status_code=201)
async def create_new_expense(body: ExpenseCreate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return await create_expense(db, current_user.id, body)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{expense_id}", response_model=ExpenseResponse, status_code=200)
async def update_expense_by_id(expense_id: int, body: ExpenseUpdate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return await update_expense(db, current_user.id, expense_id, body)
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{expense_id}", status_code=204)
async def delete_expense_by_id(expense_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return await delete_expense(db, current_user.id, expense_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))