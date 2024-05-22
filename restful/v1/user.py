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

# @router.get("/list")
# async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users