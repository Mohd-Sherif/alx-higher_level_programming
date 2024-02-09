#!/usr/bin/python3
"""Module for lookup function"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj

    Returns:
        List of available attributes and methods of an object.
    """
    return dir(obj)
