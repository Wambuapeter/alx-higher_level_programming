#!/usr/bin/python3

'''class Rectangle that inherits class Base'''

from models import base
Base = base.Base


class Rectangle(Base):
    '''private instance attributes with public getter and setter'''
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        '''get height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height'''
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''get x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set x'''
        if not isinstance(self.x, int):
            raise TypeError("x must be an integer")
        if self.x < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y'''
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
