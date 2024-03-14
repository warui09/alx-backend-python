#!/usr/bin/env python3
"""
Module to perform addition operations.

This module provides functions to add two numbers.

Functions:
    add(a: float, b: float) -> float: Adds two floats and returns the result.

Usage:
    result = add(3.4, 5.6)
    print(result)
"""


def add(a: float, b: float) -> float:
    """
    Add two floats and return the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Examples:
        >>> add(3.4, 5.6)
        9.0
    """

    return a + b
