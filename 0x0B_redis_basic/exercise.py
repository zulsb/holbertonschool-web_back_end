#!/usr/bin/env python3
""" Redis module.
"""
import redis
import uuid
from functools import wraps
from sys import byteorder
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """ Method that count calls.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **keywords):
        """ Method wrapper.
        """
        self._redis.incr(key)
        return method(self, *args, **keywords)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Method that store the history of inputs and outputs
        for a particular function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """ Method wrapper.
        """
        self._redis.rpush("{}:inputs".format(key), str(args))
        history = method(self, *args)
        self._redis.rpush("{}:outputs".format(key),
                          str(history))
        return history
    return wrapper


def replay(method: Callable):
    """ Method that display the history of calls
        of a particular function.
    """
    r = method.__self__._redis
    keys = method.__qualname__
    inputs = r.lrange("{}:inputs".format(keys), 0, -1)
    outputs = r.lrange("{}:outputs".format(keys), 0, -1)
    print("{} was called {} times:".format(keys,
                                           r.get(keys).decode("utf-8")))
    for i, j in list(zip(inputs, outputs)):
        print("{}(*{}) -> {}".format(keys, i.decode("utf-8"),
                                     j.decode("utf-8")))


class Cache:
    """ Cache class.
    """
    def __init__(self):
        """ Initializer.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(self, key: str, fn: Optional[Callable] = None):
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
