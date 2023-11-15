from app.src.adverts.schemas import SAdverts, SAdvertsBase
from app.src.categories.service import CategoryService
from fastapi import Depends
from sqlalchemy import insert, select
from app.src.adverts.models import Advertisement
from app.src.service.base import BaseService
from app.src.database import AsyncSession, async_session_maker, get_async_session

class AdvertService(BaseService):
    model = Advertisement

    def __init__(
        self,
        session: AsyncSession = Depends(get_async_session),
        category_service: CategoryService = Depends(CategoryService),
    ) -> None:
        super().__init__(session)
        self.category_service = category_service

    async def find_all(self, **filter_by)-> list[SAdverts]:
        adverts_objects = await super().find_all()
        adverts = [SAdvertsBase.from_orm(advert) for advert in adverts_objects]
        adverts_with_categories = []
        for advert in adverts:
            categories = await self.category_service.find_cats_for_advert(advert.id)
            advert_with_category = SAdverts(**advert.dict(), categories=[category.name for category in categories])
            adverts_with_categories.append(advert_with_category)
        return adverts_with_categories
    
    @classmethod
    async def add(cls):
        pass