from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    description: str | None = None

class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)