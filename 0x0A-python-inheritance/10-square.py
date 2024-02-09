#!/usr/bin/python3
"""Module for Square Class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class that defines properties of Square"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
