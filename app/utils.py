from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def password_hash(password: str): 
   
    return pwd_context.hash(password)

# function to verify passwords 

def verify(plain_password, hashed_password): 

    return pwd_context.verify(plain_password, hashed_password)