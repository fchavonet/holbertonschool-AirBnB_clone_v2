#!/usr/bin/python3
"""Define DBStorage engine"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Private class attributes"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        try:
            if getenv("HBNB_ENV") == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        storage = {}
        valid_classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            for cls in valid_classes:
                for instance in self.__session.query(cls):
                    storage["{}.{}".format(
                        cls.__name__, instance.id)] = instance
        else:
            if cls in valid_classes:
                for instance in self.__session.query(cls):
                    storage["{}.{}".format(
                        cls.__name__, instance.id)] = instance

        return storage

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

    def reload(self):
        """Create all tables and initialize the session"""

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Closes the current session"""
        self.__session.remove()
