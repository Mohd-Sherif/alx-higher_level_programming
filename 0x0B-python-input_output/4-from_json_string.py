#!/usr/bin/python3
"""Module from_json_string method"""

import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string"""
    return json.load(my_str)
