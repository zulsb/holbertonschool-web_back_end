#!/usr/bin/env python3
"""fgdgdgdgdgfggf
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """sfsfsdffggfhf
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """dsdsdfsghfhfh
        """
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """sdffssffghfh
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """sfffsdfghf
        """
        return None
