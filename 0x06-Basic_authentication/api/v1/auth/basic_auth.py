#!/usr/bin/env python3
""" BasicAuth module.
"""
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Class to manage the API authentication that inherits from Auth.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that extract the Base64 part of the authorization header.
            Arg:
                authorization_header: string type.
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
                                        self, base64_authorization_header: str
                                            ) -> str:
        """ Method that decode the Base64 part of the authorization header.
            Arg:
                authorization_header: string type.
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64_authorization_header = base64.b64decode(
                                            base64_authorization_header)
        except Exception:
            return None
        return base64_authorization_header.decode("utf-8")

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Method that extract user credentials from the Base64 decoded value.
            Arg:
                decoded_base64_authorization_header: string type.
            Return:
                The user email and password.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) is not str:
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(":")
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar("User"):
        """ Method that returns the user instance based on email and password.
            Args:
                user_email: string type.
                user_pwd: string type.
            Return:
                User instance or none.
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return None
        if not user or len(user) == 0:
            return None
        if not user[0].is_valid_password(user_pwd):
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar("User"):
        """ Method that overloads Auth and retrieves the
            user instance for a request.
        """
        authHeader = self.authorization_header(request=request)
        extB64 = (self.extract_base64_authorization_header(authHeader))
        decodeB64 = (self.decode_base64_authorization_header(extB64))
        extractUser = self.extract_user_credentials(decodeB64)
        userObject = self.user_object_from_credentials(
            user_email=extractUser[0],
            user_pwd=extractUser[1])
        return userObject
