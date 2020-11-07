#!/usr/bin/env python3
""" Auth class.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method
            Args:
                path: String type.
                excluded_paths: List type.
            Return:
                True if the path is not in the list of strings.
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method to validate all requests to protect the API.
            Args:
                request.
            Return:
                None - request.
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method
            Args:
                request.
            Return:
                None - request.
        """
        return None
