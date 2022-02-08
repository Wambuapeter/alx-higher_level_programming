#!/usr/bin/python3
'''create an object from json file'''


def load_from_json_file(filename):
    '''create an object from json file'''
    with open(filename, encoding='utf-8') as myFile:
        my_json_file_contains = read(myFile)
        object1 = json.loads(my_json_file_contains)
    return object1
