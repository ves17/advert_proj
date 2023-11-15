from app.src.adverts.schemas import SAdverts, SAdvertsBase
from app.src.adverts.service import AdvertService
from app.src.users.dependecies import get_current_user
from app.src.users.models import User
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/advertisments",
    tags=["Объявления"],
)


@router.get("")
async def get_adverts(
    advert_service: AdvertService = Depends(AdvertService),
    user: User = Depends(get_current_user)
    ):
    return await advert_service.find_all(author=user.id)


@router.get("/{advert_id}")
async def get_advert_by_id(
    advert_id: int, 
    advert_service: AdvertService = Depends(AdvertService)
) -> SAdvertsBase:
    return await advert_service.find_by_id(int(advert_id))

@router.post("/add")
async def add_advert(
    advert_data: SAdverts,
    user: User = Depends(get_current_user),
    advert_service: AdvertService = Depends(AdvertService)
    ):
    await advert_service.add()