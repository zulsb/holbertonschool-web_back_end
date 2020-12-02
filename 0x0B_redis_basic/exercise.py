#!/usr/bin/env python3
""" Redis module.
"""
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class.
    """
    def __init__(self):
        """ Initializer.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that generate a random key,
            store the input data in Redis using the random key.
            Arg:
                data: Can be a str, bytes, int or float.
            Return:
                The key as string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
