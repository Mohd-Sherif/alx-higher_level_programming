#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
