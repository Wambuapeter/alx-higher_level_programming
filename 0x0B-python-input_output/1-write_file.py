#!/usr/bin/python3
'''writes on a text file'''


def write_file(filename="", text=""):
    '''write and return length of string written'''
    with open(filename, mode="w" encoding="UTF8") as myFile:
        return myFile.write(text)
