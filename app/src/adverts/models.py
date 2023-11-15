from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.src.database import Base


class Advertisement(Base):
    __tablename__="advertisement"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # type = Column(String, nullable=False)
    text = Column(String, nullable=False)
    author = Column(ForeignKey("user.id"))
    date = Column(Date, nullable=False)
