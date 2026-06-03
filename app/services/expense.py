from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate

async def create_expense(db: AsyncSession, user_id: int, data: ExpenseCreate) -> Expense:
    expense = Expense(
        name=data.name,
        amount=data.amount,
        note=data.note,
        expense_date=data.expense_date,
        user_id=user_id,
        category_id=data.category_id
    )
    db.add(expense)
    await db.commit()
    await db.refresh(expense)

    return expense

async def get_expenses(db: AsyncSession, user_id:int) -> list[Expense]:
    result = await db.execute(select(Expense).where(Expense.user_id == user_id))
    return list(result.scalars().all())

async def get_expense(db: AsyncSession, user_id: int, expense_id: int) -> Expense:
    result = await db.execute(select(Expense).where(Expense.id == expense_id, Expense.user_id == user_id))
    return result.scalar_one_or_none()

async def update_expense(db: AsyncSession, user_id: int, expense_id: int, data: ExpenseUpdate) -> Expense:
    expense = await get_expense(db, user_id, expense_id)
    if not expense:
        raise ValueError(f"Expense not found")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(expense, field, value)

    await db.commit()
    await db.refresh(expense)
    return expense

async def delete_expense(db: AsyncSession, user_id: int, expense_id: int) -> None:
    expense = await get_expense(db, user_id, expense_id)
    if not expense:
        raise ValueError("Expense not found")
    await db.delete(expense)
    await db.commit()

