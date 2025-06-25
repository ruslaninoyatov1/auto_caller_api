from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import QarzdorCreate
from app.database import SessionLocal
from app.models import Qarzdor
from app.auth import verify_api_key

router = APIRouter(tags=["Qarzdor"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/qarzdor", summary="Qarzdor ma’lumotini qo‘shish", dependencies=[Depends(verify_api_key)])
def create_qarzdor(payload: QarzdorCreate, db: Session = Depends(get_db)):
    new = Qarzdor(
        qarzdorlik_mazmuni=payload.qarzdorlik_mazmuni,
        aloqa=payload.aloqa.dict(),
        tolov_listi=[item.dict() for item in payload.tolov_listi],
        qilingan_tolovlar=[item.dict() for item in payload.qilingan_tolovlar]
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return {"message": "Qo‘shildi", "id": new.id}
