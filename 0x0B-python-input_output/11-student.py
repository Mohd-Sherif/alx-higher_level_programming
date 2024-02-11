#!/usr/bin/python3
"""Module Student Class"""


class Student:
    """Define Student Class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr_name in attrs:
            if isinstance(attr_name, (str, int)) and hasattr(self, attr_name):
                json_dict[attr_name] = getattr(self, attr_name)
        return json_dict

    def reload_from_json(self, json):
        for attr_name, attr_value in json.items():
            setattr(self, attr_name, attr_value)
