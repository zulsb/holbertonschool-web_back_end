#!/usr/bin/env python3
""" BasicAuth module.
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class to manage the API authentication that inherits from Auth.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that returns the Base64 part of the authorization header.
            Arg:
            authorization_header: string type.
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]
