from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base

from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Union 


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(60))
    user_pw = Column(String(400))
    dep_id = Column(Integer,ForeignKey("department.id"))
    security_grade = Column(Integer, default=0)
    
    # 보안등급 정책
    # 0 = no access
    # 1 = 사내 서버
    # 2 = 사내+QA서버
    # 3 = 사내+QA+Prd서버
    # 4 = 3+데이터베이스서버
    # 5 = Admin

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    department_name = Column(String)

# Pydantic
class UserBaseType(BaseModel):
    user_id: str

class UserType(UserBaseType):
    id: int
    is_active: bool 
    class Config:
        orm_mode = True

class UserCreateType(UserBaseType):
    password: str

# User Crud Model 
class UserModel:
    def __init__(self):
        pass

    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    def create_user(db: Session, user: UserType):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(user_id=user.user_id, hashed_password=fake_hashed_password)
        db.add(db_user)  # DB에 해당 인스턴스 추가하기
        db.commit()  # DB의 변경 사항 저장하기
        db.refresh(db_user)  # 생성된 ID와 같은 DB의 새 데이터를 포함하도록 새로고침
        return db_user