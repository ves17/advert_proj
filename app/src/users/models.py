from sqlalchemy import Column, Integer, Boolean, String

from app.src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean)
    password = Column(String, nullable=False)
