#!/usr/bin/python3
'''appends text to a file'''


def append_write(filename="", text=""):
    '''append at the end the text'''
    with open(filename, encoding="UTF8") as myFile:
        return myFile.append(text)
