#!/usr/bin/python3


import csv
import json
import os


class Base:
    '''base of all my classes in the project'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initializes the class'''
        if self.id is not None:
            Base. __nb_objects += 1
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns json string rep of a list of dictionaries'''
        if (list_dictionaries is None or len(list_dictionaries == 0)):
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes json rep to a file'''
        filename = cls.__name__ + '.json'
        with open(filename, mode='w' encoding='utf-8') as myFile:
            new_list = []
            if list_objs is None:
                myFile.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(obj.to_json_string())
                myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''returns list of json string representation'''
        if json_string is None or len(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes set'''
        dummy_instance = cls(2, 3, 4, 5)
        clas.update(dummy_instance, **dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''returns a list of insatnces'''
        instance_list = []
        filename = cls.__name__ + '.json'
        if os.path.exists(filename) is False:
            return instance_list
        with open(filename, mode='w', encoding='utf-8') as myFile:
            objs = cls.from_json_string(myFile.read())
            for obj in objs:
                instance_list.append(cls.create(**obj))
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes in CSV'''
        filename = cls.__name__ + ".csv"
        with open(filename, mode='r') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ = "Square":
                csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes in csv'''
        filename = cls.__name__ + ".csv"
        myList = []
        try:
            with open(filename, mode='r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    myList.append(obj)
        except:
            pass
        return myList
