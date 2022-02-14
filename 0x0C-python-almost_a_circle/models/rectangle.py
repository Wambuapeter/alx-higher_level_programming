#!/usr/bin/python3

"""class Rectangle that inherits class Base"""

from models import base
Base = base.Base


class Rectangle(Base):
    """private instance attributes with public getter and setter"""
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get width"""
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
        """ get value """

        return self.__height

    @height.setter
    def height(self, height):
        """set value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ get value """
        return self.__x

    @x.setter
    def x(self, x):
        """set value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ get value """
        return self.__y

    @y.setter
    def y(self, y):
        """set value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area of rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with #"""
        print('\n' * self.__y, end='')

        for i in range(self.height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """returns some specified value"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the private attributes"""
        rectangle_attrs = ["id", "width", "height", "x", "y"]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                if k in rectangle_attrs:
                    setattr(self, k, v)
        else:
            for i in range(len(args)):
                setattr(self, rectangle_attrs[i], args[i])

    def to_dictionary(self):
        """return a dictionary of the rectangle"""
        rectangle_dict = {'id': self.id, 'width': self.__width,
                          'height': self.__height,
                          'x': self.__x, 'y': self.__y}
        return rectangle_dict
