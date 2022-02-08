#!/usr/bin/python3
"""appends text to a file"""


def append_write(filename="", text=""):
    """append at the end the text"""
    with open(filename, mode='a', encoding='utf-8') as myFile:
        return myFile.write(text)
