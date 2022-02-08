#!/usr/bin/python3
'''write to a file using json'''


def save_to_json_file(my_obj, filename):
    '''write by json'''
    with open(filename, mode='w', encoding='utf-8') as f:
        my_json_file = json.dumps(my_obj)
        f.write(my_json_file)
