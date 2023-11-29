#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60),
           ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60),
           ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
    else:
        @property
        def reviews(self):
            """ Getter attribute for reviews in FileStorage """
            from models import storage

            review_list = []
            for review in storage.all(Review).values():
                if self.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter attribute for amenities in FileStorage"""
            from models import storage

            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if self.amenity_ids == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute for amenities in FileStorage"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
