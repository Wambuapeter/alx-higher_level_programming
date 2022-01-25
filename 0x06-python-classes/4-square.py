#!/usr/bin/python3
'''defines a square.'''


class Square:
    '''represent a square.'''
    def __init__(self, size=0):
        '''
        args:
        size(of type int).
        '''
        self.__size = size

        @property
        def size(self):
            '''returns current size'''
            return(self.__size)

        @size.setter
        def size(self):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        '''returns area of square'''
        return(self.__size * self.__size)
