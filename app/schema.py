from typing import Optional
from pydantic import BaseModel, EmailStr



class Product(BaseModel): 
    title: str 
    description: str 

class productOut(Product): 
  
    class Config: 
        orm_mode = True

class User(BaseModel): 
    name: str
    email: EmailStr
    password: str


class Login(BaseModel): 
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str 

class TokenData(BaseModel): 
    id: Optional[str] = None
