#!/usr/bin/python3
"""Defines a printing square function"""


def print_square(size):
    """
    Print a square represented by `#`

    :param size: of the square
    :raises: TypeError: If size is not an integer
    :raises: ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("#" * size) for i in range(size)]
