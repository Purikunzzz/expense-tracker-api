from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.services.summary import get_monthly_summary
from app.schemas.summary import MonthlySummaryResponse
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/summary", tags=["summary"])

@router.get("/", response_model=MonthlySummaryResponse, status_code=200)
async def get_summary(
        month: int | None = None,
        year: int | None = None,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(get_current_user)
):
    now = datetime.now()
    month = month or now.month
    year = year or now.year
    try:
        result = await get_monthly_summary(db, current_user.id, month, year)
        if not result:
            raise HTTPException(status_code=404, detail="summary not found")
        return result
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
