from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError
from typing import Optional
from datetime import datetime
from models.models import User, Account
from flask_babel import _

class SavingBase(BaseModel):
    name: str
    description: Optional[str] = None
    amount: float
    date: datetime
    category_id: int = Field(..., gt=0)
    place_id: int = Field(..., gt=0)
    user_id: int = Field(..., gt=0)
    currency: str
    
class SavingRead(SavingBase):
    id: int

    class Config:
        from_attributes = True

class SavingCreate(SavingBase):
    @field_validator('category_id', 'place_id', 'user_id')
    @classmethod
    def validate_foreign_key(cls, v, info):
        db = info.context.get('db')
        if not db:
            raise ValueError("DATABASE_NOT_AVAILABLE")

        model_map = {
            'category_id': SavingsCategory,
            'place_id': Place,
            'user_id': User
        }

        model = model_map[info.field_name]
        if not db.query(model).filter(model.id == v).first():
            #raise ValueError(f"{info.field_name.upper()}_NOT_FOUND")
            raise PydanticCustomError("FK_ERROR", f"{info.field_name.upper()}_NOT_FOUND")
        return v

class SavingUpdate(SavingBase):
    name: Optional[str]
    description: Optional[str] = None
    amount: Optional[float]
    date: Optional[datetime]  # Use str for date representation (ISO format)
    category_id: Optional[int]
    place_id: Optional[int]
    user_id: Optional[int]
    currency: Optional[str]  
    # Optional fields

class SavingDelete(BaseModel):
    pass

