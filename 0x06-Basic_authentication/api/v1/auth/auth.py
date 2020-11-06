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
                False - path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method
            Args:
                request.
            Return:
                None - request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method
            Args:
                request.
            Return:
                None - request.
        """
        return None
