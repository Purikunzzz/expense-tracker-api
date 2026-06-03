from pydantic import BaseModel, ConfigDict
from datetime import datetime, date
from decimal import Decimal

class ExpenseCreate(BaseModel):
    name: str
    amount: Decimal
    expense_date: date
    note: str | None = None
    category_id : int

    
class ExpenseUpdate(BaseModel):
    name: str | None = None
    amount: Decimal | None = None
    expense_date: date | None = None
    note: str | None = None
    category_id: int | None = None

class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    category_id: int
    name: str
    amount: Decimal
    expense_date: date
    note: str | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
