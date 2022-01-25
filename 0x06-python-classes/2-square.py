#!/usr/bin/python3
'''defines a square.'''


class Square:
    '''represent a square.'''
    def __init__(self, size):
        '''
        args:
        size(of type int).
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
