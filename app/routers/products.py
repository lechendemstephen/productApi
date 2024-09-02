
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter


from .. import models, schema, oauth2
from sqlalchemy.orm import Session 
from ..database import get_db


router = APIRouter(
     prefix= "/products",
     tags= ['Products']
)





# getting all products 
@router.get("/")
def get_products(db: Session = Depends(get_db),  user_id : int = Depends(oauth2.get_current_user)): 
     products = db.query(models.Product).all()

     return {
          "all": products
     }



# creating a product 
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_product(product:schema.Product, db: Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)): 
     
     
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
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_product(id: int, db: Session = Depends(get_db),  user_id : int = Depends(oauth2.get_current_user)): 
     
     product = db.query(models.Product).filter(models.Product.id == id).first()

     if product == None: 
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id: {id} not found')
     
     return {
          "single Product": product
     }

# deleting a particular post based on Id 
@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db),  user_id : int = Depends(oauth2.get_current_user)): 
    
    product = db.query(models.Product).filter(models.Product.id == id).first()


    if product == None: 
         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'product with id: {id}, not found')
    
    db.delete(product)
    db.commit()
    
    return {
         "deleted product": product, 
         
    }

# updating a particular based in ID 
@router.put("/{id}")
def product_up(id: int , product: schema.Product, db: Session = Depends(get_db),  user_id : int = Depends(oauth2.get_current_user)): 
     
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

