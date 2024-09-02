from fastapi import FastAPI, HTTPException, status, Depends, APIRouter


from .. import models, schema, utils
from sqlalchemy.orm import Session 
from ..database import get_db


router = APIRouter(
     prefix= "/users",
     tags=['Users']
)


# creating a user 

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: schema.User, db: Session = Depends(get_db)): 
     
     # hashing password 
     try: 
        hashed_password = utils.password_hash(user.password)
        user.password = hashed_password
     except Exception as e: 
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'unable to hash password error: {e}')

     new_user = models.User(
          **user.dict()
     )

     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     return {
          "new user": new_user
     }
          

