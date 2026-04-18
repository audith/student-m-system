from datetime import datetime,timedelta
from passlib.context import CryptContext
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"

pwd_context=CryptContext(schemes=["argon2"],deprecated="auto")


def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_token(data:dict):
    to_encode=data.copy()
    to_encode.update({"exp":datetime.utcnow()+timedelta(minutes=60)})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)