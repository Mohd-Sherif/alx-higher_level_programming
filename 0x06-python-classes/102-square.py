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
        self.size = size

    @property
    def size(self):
        """Getter the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter the current size with some constrains"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of the square

        Return:
            int: current square area
        """
        return self.size ** 2

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()
