#!/usr/bin/python3
"""Define DBStorage engine"""

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import create_engine
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """Private class attributes"""

__engine = None
__session = None

def __init__(self):
    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                  .format(getenv("HBNB_MYSQL_USER"),
                                    getenv("HNBN_MYSQL_PWD"),
                                    getenv("HBNB_MYSQL_HOST"),
                                    getenv("HBNB_MYSQL_DB")),
                                    pool_pre_ping=True)
    
    if getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(self.__engine)

def all(self, cls=None):
    """Query on the current database session"""

    if cls is None:
        objects = self.__session.query(BaseModel).all()
    else:
        objects = self.__session.query(cls).all()

    obj_dict = {}
    for obj in objects:
        key = "{}.{}".format(type(obj).__name__, obj.id)
        obj_dict[key] = obj

    return obj_dict

def new(self, obj):
    """add the object to the current database session """
    self.__session.add(obj)

def save(self):
    """commit all changes of the current database session"""
    self.__session.commit()

def delete(self, obj=None):
    """delete from the current database session"""
    if obj is not None:
        self.__session.delete(obj)
