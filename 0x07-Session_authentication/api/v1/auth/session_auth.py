#!/usr/bin/env python3
""" SessionAuth module.
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Class to manage the API authentication that inherits from Auth.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that creates a Session ID for a user_id.
            Arg:
                user_id: string type.
        """
        if user_id is None or type(user_id) is not str:
            return None
        sessionID = str(uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Method for storing and retrieving a link between a
            User ID and a Session ID.
            Arg:
                user_id: string type.
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Method that returns a User instance based on a cookie value.
        """
        sessionID = self.session_cookie(request)
        try:
            return User.get(id=self.user_id_for_session_id(sessionID))
        except Exception:
            return None

    def destroy_session(self, request=None):
        """ Method that deletes the user session/logout.
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        if not self.user_id_for_session_id(session_id):
            return False
        del self.user_id_by_session_id[session_id]
        return True
