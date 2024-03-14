#!/usr/bin/env python3
"""
Return a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return multiplier function
    """

    return lambda num: num * multiplier
