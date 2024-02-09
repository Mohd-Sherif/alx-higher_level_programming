#!/usr/bin/python3
"""Module for MyInt Class"""


class MyInt(int):
    """Class that defines properties of MyInt"""

    def __init__(self, n):
        self.__n = n

    def __eq__(self, other):
        return not (self.__n == other)

    def __ne__(self, other):
        return not (self.__n != other)

    def __str__(self):
        return "{}".format(self.__n)
