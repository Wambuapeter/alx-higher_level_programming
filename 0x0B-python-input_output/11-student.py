#!/usr/bin/python3
"""class Student that defines a student"""


class Student:

    """Public instance attributes: first_name, last_name, age"""

    def __init__(self, first_name, last_name, age):

        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """retrieves a dictionary representation of a Student instance"""

        if attrs is None or type(attrs) is not list:

            return self.__dict__

        new_dict = {}

        for attr in attrs:

            if type(attr) is not str:

                return self.__dict__

            if attr in self.__dict__:

                new_dict[attr] = self.__dict__[attr]

        return new_dict

    def reload_from_json(self, json):

        """replaces all attributes of the Student instance"""

        for attr in json:
            self.__dict__[attr] = json[attr]
