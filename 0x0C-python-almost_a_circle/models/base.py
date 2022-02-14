#!/usr/bin/python3

"""This class will be the base of all other classes in this project."""

import os
import json


class Base:

    """private class attribute __nb_objects = 0"""
    """class constructor: def __init__(self, id=None)"""

    __nb_objects = 0

    def __init__(self, id=None):

        """if id is not None, assign the public instance attribute id """
        """with this argument value, otherwise, increment __nb_objects"""
        """and assign the new value to the public instance attribute id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as f:
            new_list = []
            if list_objs is None:
                f.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_inst = cls(1, 2, 3, 4)
        cls.update(dummy_inst, **dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        inst_list = []
        filename = cls.__name__ + '.json'
        if os.path.exists(filename) is False:
            return inst_list
        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            for obj in objs:
                inst_list.append(cls.create(**obj))
            return inst_list
