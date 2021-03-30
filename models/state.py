#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBN_TYPE_STORAGE") == "db":
        cities = relationship("City", backref=backref("state",
                                                      cascade="all,
                                                      delete-orphan",
                                                      single_parent=True))
    elif getenv("HBN_TYPE_STORAGE") == "fs":
        @property
        def cities(self):
            """Method to get a list of City instances
            with state_id equals to current State.id"""
            cities_list = []
            cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
