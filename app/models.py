from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, text

class Product(Base): 
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base): 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    jioned_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



