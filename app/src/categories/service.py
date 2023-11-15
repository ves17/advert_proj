from app.src.categories.schemas import SCategory
from app.src.service.base import BaseService
from app.src.categories.models import Category, AdvertisementsCategory
from app.src.database import async_session_maker
from sqlalchemy import and_, insert, select

class CategoryService(BaseService):
    model = Category
    async def find_cats_for_advert(self, advert_id:int)->list[SCategory]:
        query = select(self.model).join(
            AdvertisementsCategory,
            and_(
                AdvertisementsCategory.id_advert == advert_id,
                AdvertisementsCategory.id_category == self.model.id
            )
        )
        result = await self.session.execute(query)
        return result.scalars().all()
