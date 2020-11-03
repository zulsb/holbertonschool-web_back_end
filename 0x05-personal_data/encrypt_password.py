#!/usr/bin/env python3
""" Personal data.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that encrypting passwords.
        Arg:
            password: one string argument.
        Returns:
            A byte string.
    """
    return bcrypt.hashpw(bytes(password, "ascii"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function that check is valid password.
        Args:
            hashed_password: bytes type.
            password: string type.
        Returns:
            A boolean.
    """
    return bcrypt.checkpw(bytes(password, "ascii"), hashed_password)
