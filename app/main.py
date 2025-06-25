from fastapi import FastAPI, HTTPException, Depends, Header
from app.schemas import QarzdorRequest
from app.database import SessionLocal, engine
from app import models
from sqlalchemy.orm import Session

app = FastAPI()

# Ma'lumotlar bazasini yaratish
models.Base.metadata.create_all(bind=engine)

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API token tekshirish uchun (oddiy variant)
def verify_token(x_api_key: str = Header(...)):
    if x_api_key != "3dc0f8d4-739a-4b31-921f-123456abcdef":
        raise HTTPException(status_code=401, detail="Noto‘g‘ri yoki mavjud bo‘lmagan API kalit")

@app.post("/api/v1/qarzdor", dependencies=[Depends(verify_token)])
def add_qarzdor(data: QarzdorRequest, db: Session = Depends(get_db)):
    # Agar siz bu ma'lumotlarni DBga saqlamoqchi bo‘lsangiz, bu yerga yoziladi.
    # Hozircha faqat response qaytaramiz.
    return {
        "message": "Qarzdor ma'lumotlari saqlandi",
        "data": data
    }
