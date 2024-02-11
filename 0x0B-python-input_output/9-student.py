#!/usr/bin/python3
"""Module Student Class"""


class Student:
    """Define Student Class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        json_dict = {}
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
        return json_dict
