#!/usr/bin/python3
"""Module for MyList Class"""


class MyList(list):
    """Class that defines properties of MyList."""

    def __init__(self):
        """Creates new instances of MyList."""
        super()

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
