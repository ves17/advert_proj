

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
load_dotenv(dotenv_path = "app/src/.env")

db_user = os.environ.get("POSTGRES_USER")
db_password = os.environ.get("POSTGRES_PASSWORD")
db_name = os.environ.get("POSTGRES_DB")
db_host = os.environ.get("POSTGRES_HOST")
db_port = os.environ.get("POSTGRES_PORT")
# print(f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

database_url = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# database_url1 = f"postgresql://postgres:1234@localhost:5432/ads"
# f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_async_engine(database_url, pool_pre_ping=True)

async_session_maker = async_sessionmaker(bind = engine, class_=AsyncSession, autocommit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass