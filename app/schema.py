from pydantic import BaseModel



class Product(BaseModel): 
    title: str 
    description: str 

class productOut(Product): 
  
    class Config: 
        orm_mode = True
