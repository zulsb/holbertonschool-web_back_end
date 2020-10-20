#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Type-annotated function sum_mixed_list that takes a list of
        float and integers arguments.
        Args:
            mxd_lst: float and int type.
        Return:
            The sum as a float.
    """
    return sum(mxd_lst)
