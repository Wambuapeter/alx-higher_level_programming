#!/usr/bin/python3
'''defines a square.'''


class Square:
    '''represent a square.'''
    def __init__(self, size=0):
        '''
        args:
        size(of type int).
        '''
        self.size = size

    @property
    def size(self):
        '''sets current size'''
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''returns area of square'''
        return(self.__size * self.__size)
