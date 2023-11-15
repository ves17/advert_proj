from typing import Type
from app.src.database import AsyncSession, get_async_session
from fastapi import Depends
from sqlalchemy import insert, select
from app.src.database import Base


class BaseService():
    model: Base
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session

    async def find_by_id(self, model_id: int):
        try:
            query = select(self.model).filter_by(id = model_id)
            result = await self.session.execute(query)
            return result.scalar_one_or_none()
        except Exception as e:
            print(f"Произошла ошибка при выполнении асинхронного запроса: {e}")
    
    async def find_all(self, **filter_by):
        try:
            query = select(self.model).filter_by(**filter_by)
            result = await self.session.execute(query)
            return result.scalars().all()
        except Exception as e:
            print(f"Произошла ошибка при выполнении асинхронного запроса: {e}")
    

    async def find_one_or_none(self, **filter_by):
        try:
            query = select(self.model).filter_by(**filter_by)
            result = await self.session.execute(query)
            return result.scalar_one_or_none()
        except Exception as e:
            print(f"Произошла ошибка при выполнении асинхронного запроса: {e}")
    
    
    async def add(self, **data):
        try:
            query = insert(self.model).values(**data)
            await self.session.execute(query)
            await self.session.commit()
        except Exception as e:
            print(f"Произошла ошибка при выполнении асинхронного запроса: {e}")