#!/usr/bin/python3
"""Module class_to_json method"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("Object does not have a __dict__ attribute")
    json_dict = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value
    return json_dict
