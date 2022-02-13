#!/usr/bin/python3

from models import base
Base = base.Base


class Rectangle(Base):
    '''inherits class Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        if self.width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(self.x, int):
            raise TypeError("x must be an integer")
        if self.x < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(self.y, int):
            raise TypeError("y must be an integer")
        if self.y < 0:
            raise ValueError("height must be >= 0")
        self.__y = value

    def area(self):
        '''returns area value of the Rectangle instance'''
        return (self.__width * self.__height)

    def display(self):
        '''prints in stdout the rectangle instance with #'''
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        '''returns some specified value'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''updates the private attributes'''
        rect_attr = [id, width, height, x, y]
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key in rect_attr:
                    setattr(self, key, value)
        else:
            for i in range(len(args)):
                setattr(self, rect_attr[i], args[i])

    def to_dictionary(self):
        '''returns dictionary representation of the reactangle'''
        rect_dict = {'id': self.id, 'width': self.__width,
                     'height': self.__height,
                     'x': self.__x, 'y': self.__y}
        return rect_dict
