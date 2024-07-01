from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from.database import Base

class User(Base):
    __tablename__ = "users"

    id =  Column(Integer, primary_key=True)
    name = Column(String, index=True)
    username = Column(String, index=True)

    videos = relationship('Videos', back_populates="owner")

class Videos(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key = True)
    url = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="videos")