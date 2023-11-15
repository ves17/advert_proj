from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.src.database import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    id_advert = Column(ForeignKey("advertisement.id"))
    text = Column(String, nullable=False)
    author = Column(ForeignKey("user.id"))
    date = Column(Date, nullable=False)
