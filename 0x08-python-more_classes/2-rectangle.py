#!/usr/bin/python3

"""
Rectangle Class
"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Definiton """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter"""
        return 2 * (self.width + self.height)
