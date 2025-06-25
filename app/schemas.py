from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class Aloqa(BaseModel):
    phone: str
    phone2: Optional[str] = None

class Tolov(BaseModel):
    id: int
    sum: int
    left: int
    due_date: date
    status: int

class QilinganTolov(BaseModel):
    id: int
    sum: int
    date: date
    type: int
    comment: Optional[str] = None

class QarzdorRequest(BaseModel):
    qarzdorlik_mazmuni: str
    aloqa: Aloqa
    tolov_listi: List[Tolov] = Field(..., alias="to‘lov_listi")
    qilingan_tolovlar: List[QilinganTolov]

    class Config:
        allow_population_by_field_name = True 