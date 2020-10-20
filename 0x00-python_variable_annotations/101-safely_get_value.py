#!/usr/bin/env python3
""" More involved type annotations """
from typing import Any, Union, Mapping, TypeVar
F = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[F, None]) -> Union[Any, F]:
    """ Type-annotated function safe_first_element. """
    if key in dct:
        return dct[key]
    else:
        return default
