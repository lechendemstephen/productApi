from fastapi import FastAPI, HTTPException, status, Depends


from typing import List
from .database import engine, get_db
from sqlalchemy.orm import Session 
from . import models


from . import schema
from . import utils


# creating connection 
db = models.Base.metadata.create_all(bind=engine)

# fastapi instance 
app = FastAPI()



# getting all products 
@app.get("/products")
def get_products(db: Session = Depends(get_db)): 
     products = db.query(models.Product).all()

     return {
          "all": products
     }



# creating a product 
@app.post('/products', status_code=status.HTTP_201_CREATED)
def create_product(product:schema.Product, db: Session = Depends(get_db)): 
     
     new_product = models.Product(
          **product.dict()
     )
     db.add(new_product)
     db.commit()
     db.refresh(new_product)

     return {
          "New product": new_product
     }

# getting one product 
@app.get("/product/{id}", status_code=status.HTTP_200_OK)
def get_product(id: int, db: Session = Depends(get_db)): 
     
     product = db.query(models.Product).filter(models.Product.id == id).first()

     if product == None: 
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id: {id} not found')
     
     return {
          "single Product": product
     }

# deleting a particular post based on Id 
@app.delete("/product_del/{id}")
def delete_product(id: int, db: Session = Depends(get_db)): 
    
    product = db.query(models.Product).filter(models.Product.id == id).first()


    if product == None: 
         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'product with id: {id}, not found')
    
    db.delete(product)
    db.commit()
    
    return {
         "deleted product": product
    }

# updating a particular based in ID 
@app.put("/product_up/{id}")
def product_up(id: int , product: schema.Product, db: Session = Depends(get_db)): 
     
     update_product = db.query(models.Product).filter(models.Product.id == id ).first()

     if update_product == None: 
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'product with id {id}, not found')
     
     for key, value in product.dict().items(): 
          if value is not None: 
               setattr(update_product, key, value)
     db.commit()
     db.refresh(update_product)

     return {
          " Updated post": update_product
     }


# creating a user 

@app.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(user: schema.User, db: Session = Depends(get_db)): 
     
    #  # hashing password 
    #  hashed_password = utils.hash_password(user.password)
    #  user.password = hashed_password

     new_user = models.User(
          **user.dict()
     )

     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     return {
          "new user": new_user
     }
          
    





