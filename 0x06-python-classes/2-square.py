#!/usr/bin/python3
'''defines a square.'''


class Square:
    '''represent a square'''
    def __init__(self, size=0):
        self.__size = size
    try:
        if size != int(size):
            raise TypeError
    except TypeError:
        print("size must be an integer")
    try:
        if (size < 0):
            raise ValueError
    except ValueError:
        print("size must be >= 0")
