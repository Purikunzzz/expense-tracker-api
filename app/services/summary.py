from collections import defaultdict
from sqlalchemy.ext.asyncio import AsyncSession
from decimal import Decimal
from app.models.expense import Expense
from sqlalchemy import select, extract


async def get_monthly_summary(
        db: AsyncSession,
        user_id: int,
        month: int,
        year: int
) -> dict:
    month_year = select(Expense).where(
        Expense.user_id == user_id,
        extract("month", Expense.expense_date) == month,
        extract("year", Expense.expense_date) == year
        )

    
    result = await db.execute(month_year)
    expenses = list(result.scalars().all())
    category_totals = defaultdict(Decimal)
    for expense in expenses:
        category_totals[expense.category_id] += expense.amount

    total_amount = sum(category_totals.values()) if category_totals else Decimal(0)
    top_category_id = max(category_totals, key=lambda k: category_totals[k]) if category_totals else None

    return {
        "month": month,
        "year": year,
        "total_amount": total_amount,
        "expense": expenses,
        "top_category_id": top_category_id
    }