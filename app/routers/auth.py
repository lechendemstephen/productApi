from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
 
from sqlalchemy.orm import Session

from .. import models, schema, utils, database, oauth2



router = APIRouter(
     tags= ['Authenticate']

)


@router.post("/login")
def login_user(login: schema.Login, db: Session = Depends(database.get_db)): 
    
     user = db.query(models.User).filter(models.User.email == login.email).first()
    
     if not user:    
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
         
     if not utils.verify(login.password, user.password): 
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
     
     # create the jwt token 
     access_token  = oauth2.create_access_token(data= {"user_id": user.id })

           
     return {
           "acces_token": access_token,
           "token_type": "bearer"
     }



