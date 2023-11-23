#!/usr/bin/python3
""" User module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'

    places = relationship("Place", cascade="all, delete", back_populates="user")
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship("Review", cascade="all, delete", back_populates="user")

