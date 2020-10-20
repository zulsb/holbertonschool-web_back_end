#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Type-annotated function safe_first_element that takes a iterable
        argument.
        Args:
            lstr: iterable object.
    """
    if lst:
        return lst[0]
    else:
        return None
