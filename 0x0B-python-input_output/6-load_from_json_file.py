#!/usr/bin/python3
'''create an object from json file'''


def load_from_json_file(filename):
    '''create an object from json file'''
    with open(filename, encoding='utf-8') as f:
        my_json_file_content = f.read()
        created_object = json.loads(my_json_file_content)
    return created_object
