from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column, BigInteger, 
    String, Text)

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(50))
    name = Column(String(50))
    photo = Column(String(150))
    phone_number = Column(String(50))
    town = Column(String(50))
    status_in_israel = Column(String(50))
    sphere = Column(String(150))
    site = Column(String(150))
    instagram = Column(String(150))
    facebook = Column(String(150))
    linkedin = Column(String(150))
    member = Column(String(150))
    hobby = Column(String(150))
    query = Column(Text)
    question = Column(Text)
