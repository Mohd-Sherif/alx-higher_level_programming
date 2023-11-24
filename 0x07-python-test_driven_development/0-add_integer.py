#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Adds two integers or floats together

    Args:
        a (int): An integer or float
        b (int): An integer or float. (Default: 98)

    Return:
        The addition of a and b as an integer.

    Raises: TypeError: If a or b is not an integer or float.
                       The error message will specify the expected type.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
