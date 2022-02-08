#!/usr/bin/python3
'''return object from json rep'''


import json


def from_json_string(my_str):
    '''return an object from json'''
    return json.loads(my_str)
