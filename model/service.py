from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Text
from sqlalchemy.orm import relationship
from db import Base

class ServerService(Base):
    __tablename__ = 'serverservice'
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    service_name = Column(String(30)) # SSH
    port = Column(Integer)
    protocol = Column(String(10))
    ctype = Column(Integer, ForeignKey('credentialstype.id'))
    user_id = Column(String(60))
    user_pw = Column(String(60))
    pem_base64 = Column(Text)
    
class CredentialType(Base):
    __tablename__ = 'credentialstype'
    id = Column(Integer, primary_key=True)
    type_name = Column(String(30))
