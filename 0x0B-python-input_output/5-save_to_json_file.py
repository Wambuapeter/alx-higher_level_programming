#!/usr/bin/python3
'''write to a file using json'''


def save_to_json_file(my_obj, filename):
    '''write by json'''
    with open(filename, mode="w", encoding="utf8") as myFile:
        text_to_file = json.dumps(my_obj)
        myFile.write(text_to_file)
