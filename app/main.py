from fastapi import FastAPI
from app.routers import qarzdor
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Qarzdorlar API", version="0.1.0")

app.include_router(qarzdor.router, prefix="/api/v1")
