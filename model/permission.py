from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base
 
class UIViewPermission(Base):
    __tablename__ = 'uiviewpermission'
    id = Column(Integer, primary_key=True)
    access_ui_id = Column(Integer, ForeignKey("uiview.id"))
    allow_dep_id = Column(Integer, ForeignKey("department.id"))
    access_security_grade = Column(Integer) # 보안 등급에 따라 UI View 접근 가능

class UIView(Base):
    __tablename__ = 'uiview'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    link_id = Column(Integer, ForeignKey("uiviewlink.id"))

class UIViewLinks(Base):
    __tablename__ = 'uiviewlink'
    link_href = Column(String(60))