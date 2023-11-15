from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.src.database import Base


class Category(Base):
    __tablename__="categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class AdvertisementsCategory(Base):
    __tablename__="avert_to_categ"
    id = Column(Integer, primary_key=True)
    id_advert = Column(ForeignKey("advertisement.id"))
    id_category = Column(ForeignKey("categories.id"))
