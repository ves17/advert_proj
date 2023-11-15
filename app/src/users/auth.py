from datetime import datetime, timedelta
from passlib.context import CryptContext
from app.src.users.service import UserService
from jose import jwt
from fastapi import Depends
from pydantic import EmailStr
from app.src.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_acces_token(data:dict)->str:
    to_encode=data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM 
    )
    return encoded_jwt


async def auth_user(email: EmailStr, password: str, user_service: UserService):
    user = await user_service.find_one_or_none(email=email)
    print(user)
    access = verify_password(password, user.password)
    # print(access)
    # print(user.id)
    if not user or not access:
        return None
    return user