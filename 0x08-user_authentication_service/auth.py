#!/usr/bin/env python3
""" Auth module.
"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments.
        Arg:
            password: string type.
        Return:
            A string.
    """
    return bcrypt.hashpw(bytes(password, "ascii"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Function that return a string representation of a new UUID.
    """
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """ Method that get session ID.
            Arg:
                email: string type.
            Return:
                The session ID.
        """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Method that find user by session ID.
            Arg:
                session_id: string type.
            Return:
                A string or None.
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Method that destroy session.
            Arg:
                user_id: string type.
            Return:
                None.
        """
        return self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Method that generate reset password token.
            Arg:
                email: string type.
            Return:
                A string.
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method that update password.
            Args:
                reset_token: string type.
                password: string type.
            Return:
                None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id,
                                 reset_token=None,
                                 hashed_password=hashed_password)
        except Exception:
            raise ValueError()
