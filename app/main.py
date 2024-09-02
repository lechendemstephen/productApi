from fastapi import FastAPI, HTTPException, status, Depends


from typing import List
from .database import engine, get_db
from sqlalchemy.orm import Session 
from . import models


from . import schema
from . import utils

from .routers import products, user, auth


# creating connection 
db = models.Base.metadata.create_all(bind=engine)

# fastapi instance 
app = FastAPI()

app.include_router(products.router)
app.include_router(user.router)
app.include_router(auth.router)





