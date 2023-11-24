#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Implement `Square` Class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with the given size

        Args:
            size (int): Size of the square
            position (tuple): Locate the position of square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter the current position with some constrains"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """prints in stdout the square with the character `#`"""
        if self.size == 0:
            print()
        else:
            [print() for i in range(self.position[1])]
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
