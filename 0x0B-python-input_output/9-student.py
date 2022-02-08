#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """
    defines a student by
    public instance attributes(first_name, last_name, age):
    """

    def __init__(self, first_name, last_name, age):
        """representation of a student.
        initialization of public variables.
        """
        first_name = self.first_name
        last_name = self.last_name
        age = self.age

    def to_json(self):
        """returns the class as a dictionary descrpition"""
        return self.__dict__
