

import email
from app.src.users.auth import auth_user, create_acces_token, get_password_hash
from app.src.users.dependecies import get_current_user, get_current_user_admin
from app.src.users.models import User
from app.src.users.schemas import SUserAuth
from app.src.users.service import UserService
from fastapi import APIRouter, Depends, HTTPException, Response, status


router =APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

@router.post("/register")
async def register_user(
    user_data: SUserAuth,
    user_service: UserService = Depends(UserService)    
):
    # return user_service.register(user_data)
    existing_user = await user_service.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await user_service.add(email=user_data.email, 
                          password=hashed_password, 
                         )

@router.post("/login")
async def login(
    response: Response, 
    user_data: SUserAuth, 
    user_service: UserService = Depends(UserService)
):
    user = await auth_user(user_data.email, user_data.password, user_service)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_acces_token({"sub": str(user.id)})
    response.set_cookie("averts_access_token", access_token, httponly=True)
    return access_token

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("averts_access_token")

@router.get("/me")
async def read_users_me(user: User = Depends(get_current_user)):
    return user

@router.get("/all")
async def get_all_users(
    user: User = Depends(get_current_user_admin), 
    user_service: UserService = Depends(UserService) 
    ):
    return await user_service.find_all()
    

