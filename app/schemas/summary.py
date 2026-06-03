from pydantic import BaseModel
from decimal import Decimal
from app.schemas.expense import ExpenseResponse

class MonthlySummaryResponse(BaseModel):
    month: int
    year: int
    total_amount: Decimal
    expense: list[ExpenseResponse]
    top_category_id: int | None = None


