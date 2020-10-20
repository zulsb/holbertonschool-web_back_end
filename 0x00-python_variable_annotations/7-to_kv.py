#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Type-annotated function to_kv that takes
        strings, integers and floats arguments.
        Args:
            k: string type.
            v: int or float type.
        Return:
            Tuple.
    """
    return (k, pow(v, 2))
