#!/usr/bin/python3
"""Module for BaseGeometry Class"""


class BaseGeometry():
    """Class that defines properties of BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
