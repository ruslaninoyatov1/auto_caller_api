from fastapi import FastAPI
from app.schemas import QarzdorRequest

app = FastAPI()

@app.post("/api/v1/qarzdor")
def add_qarzdor(data: QarzdorRequest):
    return {"message": "Qarzdor ma'lumotlari saqlandi", "data": data}
