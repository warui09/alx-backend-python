#!/usr/bin/env python3
"""
Module to perform concat operations.

This module provides a function to concat two strings.

Functions:
    concat(str1: str, str2: str) -> str: concats two strings and returns a string.

Usage:
    str3 = concat('Hello', 'World')
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two trings and return the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        string: The result of concatenating str2 to str1.

    Examples:
        >>> concat('Hello', 'World')
        Hello World
    """

    return str1 + str2
