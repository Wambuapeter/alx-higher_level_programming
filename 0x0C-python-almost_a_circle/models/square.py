#!/usr/bin/python3

from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    '''inheritrs from class Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''calls the super class'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.size

    @size.setter
    '''sets width and height to same value'''
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''the overloading method'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        '''updates the private attributes'''
        square_attr = [id, size, x, y]
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key in square_attr:
                    setattr(self, key, value)
        else:
            for i in range(len(args)):
                setattr(self, square_attr[i], args[i])

    def to_dictionary(self):
        '''returns dictionary representation of the square'''
        square_dic = {'id': self.id, 'size': self.size,
                      'x': self.x, 'y': self.y}
        return square_dic
