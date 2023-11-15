from fastapi import Depends

from app.src.database import AsyncSession, Base, get_async_session
from app.src.service.base import BaseService
from app.src.users.models import User


class UserService(BaseService):
    model = User
    # read_schema: Type[BaseModel] = SUserAuth
    # write_schema: Type[BaseModel] = SUserUpdate

    # async def register(self, user_data: SUserCreate) -> SUserAuth:
    #     password_hash = get_password_hash(user_data.password)
    #     create_data = SUserCreateDB(password=password_hash, **user_data.dict(exclude={"password"}))
    #     return await self.repo.create(create_data)

# repository

# class UserRepository:
#     def __init__(self, get_session) -> None:
#         self.get_session = get_session

#     async def create(self, create_data: SUserCreateDB) -> SUserAuth:
#         async with self.get_session() as session:
#             user_obj = await session.execute(
#                 insert(User)
#                 .values(**create_data)
#                 .returning(User)
#             )
#             return SUserAuth.from_orm(user_obj)
        