#!/usr/bin/python3
"""a function that writes a string to a file"""


def write_file(filename="", text=""):
    """writes a string to a file,returns the number of characters written"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
