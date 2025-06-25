from sqlalchemy import Column, Integer, String, Date, JSON
from app.database import Base

class Qarzdor(Base):
    __tablename__ = "qarzdorlar"

    id = Column(Integer, primary_key=True, index=True)
    qarzdorlik_mazmuni = Column(String)
    aloqa = Column(JSON)
    tolov_listi = Column(JSON)
    qilingan_tolovlar = Column(JSON)
