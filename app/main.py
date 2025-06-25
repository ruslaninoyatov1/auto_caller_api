from fastapi import FastAPI
from app.schemas import QarzdorRequest

app = FastAPI(  # hech qanday o'zgartirishsiz
    title="Auto Caller API",
    version="0.1.0"
)

@app.post("/api/v1/qarzdor")
def add_qarzdor(data: QarzdorRequest):
    return {"message": "Qarzdor ma'lumotlari saqlandi", "data": data}
