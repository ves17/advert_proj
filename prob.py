


import asyncio
from sqlalchemy import select

from app.src.adverts.models import Advertisement
from app.src.database import async_session_maker

async def get_adverts_async():
    try:
        async with async_session_maker() as session:
            query = select(Advertisement)
            result = await session.execute(query)
            ads = result.fetchall()
            for ad in ads:
                print(ad.Advertisement.text)
    except Exception as e:
        print(f"Произошла ошибка при выполнении асинхронного запроса: {e}")
# asyncio.run(get_adverts_async())