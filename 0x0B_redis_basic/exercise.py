#!/usr/bin/env python3
""" Redis module.
"""
import redis
import uuid
from typing import Union, Optional, Callable
from sys import byteorder


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

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """ This callable will be used to convert
            the data back to the desired format.
            Args:
                key: string type.
                fn: Optional[Callable].
            Return:
                The convert data.
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, data: bytes) -> str:
        """ Method that get a string from bytes.
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """ Method that get a int from bytes.
        """
        return int.from_bytes(data, byteorder)
