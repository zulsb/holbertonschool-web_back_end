#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Type-annotated function make_multiplier that takes a float
        argument.
        Args:
            multiplier: float type.
        Return:
            A function that multiplies a float by multiplier.
    """
    return lambda multiplier2: multiplier2 * multiplier
