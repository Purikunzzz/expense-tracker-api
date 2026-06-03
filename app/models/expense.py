from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String(100), nullable=False)
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    expense_date = Column(Date, nullable=False)
    note = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")


