#!/usr/bin/env python3
"""
Takes a string and an int or float and returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of k and v
    """

    return (k, v ** 2)
