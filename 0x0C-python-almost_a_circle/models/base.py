#!/usr/bin/python3
"""Module for Base class"""

import csv
import json
import os

class Base:
    """
    Class that defines properties of Base.

     Attributes:
        id (int): Identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Creates new instances of Base.

        Args:
            id (int): Identity of each instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: jason string representation.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): _description_

        Returns:
            list: JSON string representation json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): double pointer to a dictionary.
            cls (any): class.

        Returns:
            list: an instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): instances who inherits of Base - example:
            list of Rectangle or list of Square instances.
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='UTF-8') as json_file:
            if not list_objs:
                json_file.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(list_of_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Args:
            cls (any): class.

        Returns:
            list: list of instances.
        """
        filename = cls.__name__ + '.json'
        list_of_instances = []

        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as json_file:
                json_str = json_file.read()
                list_of_dicts = cls.from_json_string(json_str)
                for dictionary in list_of_dicts:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
            list_objs (list): objects.
        """
        filename = cls.__name__ + '.csv'
        name = cls.__name__
        fieldnames = (['id', 'size', 'x', 'y'] if name != 'Rectangle'
                      else ['id', 'width', 'height', 'x', 'y'])
        with open(filename, 'w', newline='', encoding='UTF-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            if not list_objs:
                return
            for obj in list_objs:
                csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
        """
        filename = cls.__name__ + '.csv'
        name = cls.__name__
        fieldnames = (['id', 'size', 'x', 'y'] if name != 'Rectangle'
                      else ['id', 'width', 'height', 'x', 'y'])
        if os.path.exists(filename):
            with open(filename, 'r', newline='', encoding='UTF-8') as csv_file:
                csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                next(csv_reader)
                list_dicts = []
                for row in csv_reader:
                    new_row = {}
                    for k, val in row.items():
                        new_row[k] = int(val)
                    list_dicts.append(new_row)

                return [cls.create(**dictionary) for dictionary in list_dicts]
        return []
