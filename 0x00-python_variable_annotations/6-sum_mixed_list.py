#!/usr/bin/env python3
"""
Calculate sum of floats and integers
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of the elements of the list
    """

    return sum(mxd_lst)
