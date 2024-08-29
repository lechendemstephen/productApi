from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, text

class Product(Base): 
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    

