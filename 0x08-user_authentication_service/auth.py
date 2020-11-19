#!/usr/bin/env python3
""" Auth module.
"""
import bcrypt


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments.
        Arg:
            password: string type.
        Return:
            A string.
    """
    return bcrypt.hashpw(bytes(password, "ascii"), bcrypt.gensalt())
