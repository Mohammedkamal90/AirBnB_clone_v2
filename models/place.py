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
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:
        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances based on the attribute amenity_ids."""
            amenities_list = []
            for amenity_id in self.amenity_ids:
                amenity = models.storage.get('Amenity', amenity_id)
                if amenity:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute that handles the append method for adding an Amenity.id to the attribute amenity_ids."""
            if isinstance(amenity, models.Amenity):
                self.amenity_ids.append(amenity.id)
