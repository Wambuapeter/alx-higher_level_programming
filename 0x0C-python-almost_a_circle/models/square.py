#!/usr/bin/python3

"""this class Square inherits from Rectangle"""

from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):

    """Calls the super class with id, x, y, width and height"""

    def __init__(self, size, x=0, y=0, id=None):

        """calls the super class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):

        """the overloading method"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, size):
        """sets width and height to same value"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates the private attribute"""
        square_attrs = ["id", "size", "x", "y"]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            for i in range(len(args)):
                setattr(self, square_attrs[i], args[i])

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        square_dict = {'id': self.id, 'size': self.size,
                       'x': self.x, 'y': self.y}
        return square_dict
