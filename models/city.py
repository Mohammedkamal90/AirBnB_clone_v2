#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    __tablename__ = 'cities'
    places = relationship("Place", cascade="all, delete", back_populates="city")
