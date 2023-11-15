from pydantic import BaseModel
from datetime import date


class SAdvertsBase(BaseModel):
    id: int
    name: str
    text: str
    author: int
    date: date


    class Config:
        from_attributes=True


class SAdverts(SAdvertsBase):
    categories: list[str]