from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column, BigInteger, 
    String, Text)

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    name = Column(String(50))
    username = Column(String(50))
    phone_number = Column(String(50))
    photo = Column(String(50))
    about = Column(Text)
    family = Column(Text)
    hobby = Column(String(150))
    additional = Column(Text)