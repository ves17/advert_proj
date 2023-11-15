from app.src.adverts.schemas import SAdverts
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/categories", 
    tags=["Поиск по категориям"]
)


@router.get("/{category_id}")
async def get_adverts_by_id(category_id: int) -> list[SAdverts]:
    pass
