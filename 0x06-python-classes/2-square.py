#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Implement `Square` Class"""
    def __init__(self, size=0):
        """
        Initialize a square with the given size

        Args:
            size (int): Size of the square
        """
        if size not isinstance(int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
