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
    