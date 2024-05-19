from sqlalchemy.orm import Session
 
from db import SessionLocal, engine
from main import app
from model.user import User, Department

from fastapi import APIRouter

router = APIRouter()
@router.get("/index")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

