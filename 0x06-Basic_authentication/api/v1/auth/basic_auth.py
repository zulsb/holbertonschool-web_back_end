#!/usr/bin/env python3
""" BasicAuth module.
"""
from api.v1.auth.auth import Auth
import base64


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
