from sqlalchemy import Column, Integer, String
from db.session import Base

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(255))
    email=Column(String(255))
    password=Column(String(255))
    
