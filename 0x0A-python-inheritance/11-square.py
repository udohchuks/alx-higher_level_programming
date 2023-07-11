#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Base Geometry"""
    pass

    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


"""Rectangle """


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Initiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area"""
        return self.__width * self.__height

    def __str__(self):
        """
        [Rectangle] width/height
        """

        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


"""
Squares
"""


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """Initiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return (self.__size * self.__size)

    def __str__(self):
        """Print"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
