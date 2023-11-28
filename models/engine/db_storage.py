#!/usr/bin/python3
"""Define DBStorage engine"""

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import create_engine
from os import getenv

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
