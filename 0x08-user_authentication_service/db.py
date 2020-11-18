#!/usr/bin/env python3
""" Database module.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User


class DB:
    """ Class to manage the Database.
    """
    def __init__(self):
        """ Initializer.
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Return session.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Create and add a user to the database.
            Args:
                email: string type.
                hashed_password: string type.
            Return:
                User object.
        """
        addUser = User(email=email, hashed_password=hashed_password)
        self._session.add(addUser)
        self._session.commit()
        return addUser
