#!/usr/bin/env python3
""" Auth module.
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments.
        Arg:
            password: string type.
        Return:
            A string.
    """
    return bcrypt.hashpw(bytes(password, "ascii"), bcrypt.gensalt())


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializer.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that register user.
            Args:
                email: string type.
                password: string type.
            Return:
                User object.
        """
        try:
            self._db.find_user_by(email=email)
        except Exception:
            nUser = self._db.add_user(email, _hash_password(password))
            return nUser
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ Method that valid login.
            Args:
                email: string type.
                password: string type.
            Return:
                A boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(bytes(password, "ascii"),
                                  user.hashed_password)
        except Exception:
            return False
