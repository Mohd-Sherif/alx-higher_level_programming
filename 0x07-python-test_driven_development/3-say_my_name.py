#!/usr/bin/python3
"""Defines a printing fullname function"""


def say_my_name(first_name, last_name=""):
    """
    Print the fullname of a person

    :param first_name: arg1
    :param last_name: arg2
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
