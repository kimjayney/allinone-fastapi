from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base

class Servers(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True)
    hostname = Column(String, null=True)
    ip_addr = Column(String)
    group_id = Column(ForeignKey("servergroup.id"), ondelete='SET NULL')

class ServerGroup(Base):  
    __tablename__ = 'servergroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(60))