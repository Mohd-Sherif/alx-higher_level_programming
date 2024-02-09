#!/usr/bin/python3
"""Module for add_attribute method"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it’s possible.

    Args:
        obj
        attr_name
        attr_value
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("Can't add new attribute")
