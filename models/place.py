#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    __tablename__ = 'places'
    if models.storage_type == 'db':
        reviews = relationship("Review", cascade="all, delete", back_populates="place")
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances with place_id equals to the current Place.id."""
            reviews_list = []
            for review in models.storage.all('Review').values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
