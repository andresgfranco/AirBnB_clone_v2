#!/usr/bin/python3
"""Module for DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in a DB"""
    __engine = None
    __session = None

    def __init__(self):
        mysql_username = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        env_variable = getenv("HBNB_ENV")

        db = "mysql+mysqldb://{}:{}@{}:3306/{}".
        format(mysql_username, mysql_password, mysql_host,
               database_name)
        self.__engine = create_engine(db, pool_pre_ping=True)

        if env_variable == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session and all objects
        depending of the class"""
        classes = ["State", "City", "User", "Place", "Review", "amenity"]
        dict_all = {}
        if cls is in classes:
            query_result = self.__session.query(cls)
            for row in query_result:
                dict_all[row.__class__.__name__ + "." + row.id] = row
        else:
            query_result = self__session.query(cls).all()
            for row in query_result:
                dict_all[row.__class__.__name__ + "." + row.id] = row

        return dict_all

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit(obj)

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    defl reload(self):
        """create all tables in data bases"""
        Base.metadata.create_all(self.__engine)
        session = scoped_Session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
