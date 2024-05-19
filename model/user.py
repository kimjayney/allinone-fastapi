from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base
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
