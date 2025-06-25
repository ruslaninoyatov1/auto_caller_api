from pydantic import BaseModel
from typing import List, Optional
from datetime import date

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
    comment: str

class Aloqa(BaseModel):
    phone: str
    phone2: Optional[str]

class QarzdorCreate(BaseModel):
    qarzdorlik_mazmuni: str
    aloqa: Aloqa
    tolov_listi: List[Tolov]
    qilingan_tolovlar: List[QilinganTolov]
