#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            from models import storage
            all_cities = storage.all("City")
            state_cities = [city for city in all_cities.values()
                            if city.state_id == self.id]
            return state_cities
