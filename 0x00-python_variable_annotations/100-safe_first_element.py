#!/usr/bin/env python3
"""
Solution to task 10
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    The types of the elements of the input are not known
    """

    if lst:
        return lst[0]
    else:
        return None
