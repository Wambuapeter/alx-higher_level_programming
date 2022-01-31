#!/usr/bin/python3
'''defines a rectangle with width and height
raises exceptions
'''


class Rectangle:
    def __init__(self, width=0, height=0):
        '''defines the width and height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (height < 0):
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be > 0")
