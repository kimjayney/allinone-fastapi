from sqlalchemy.orm import Session
from db import SessionLocal, engine
from model.user import User, Department
from fastapi import APIRouter

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
@router.get("/index")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

