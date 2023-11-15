from pydantic import BaseModel, EmailStr

class SUserAuth(BaseModel):
    # id: int
    # name: str
    # is_admin: bool
    password: str
    email: EmailStr


    class Config:
        orm_mode= True


# class SUserCreate(BaseModel):
#     username: str
#     password: str


# class SUserUpdate(SUserCreate):
#     ...


# class SUserAuth(SUserUpdate):
#     id: str