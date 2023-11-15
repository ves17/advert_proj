from app.src.config import settings
from app.src.users.models import User
from app.src.users.service import UserService
from fastapi import HTTPException, Request, Depends
from jose import JWTError, jwt
from datetime import datetime

from fastapi.exception_handlers import http_exception_handler


def get_token(request: Request):
    token = request.cookies.get("averts_access_token")
    if not token:
        raise HTTPException(status_code=401, detail="No any token")
    return token

async def get_current_user(token: str = Depends(get_token), user_service: UserService = Depends(UserService)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="cant decode token")

    expire: str = payload.get("exp")
    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=401, detail="token out of time")
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="no user_id")
    user = await user_service.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="no user")
    return user

async def get_current_user_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=401, detail="Not an admin")
    return current_user