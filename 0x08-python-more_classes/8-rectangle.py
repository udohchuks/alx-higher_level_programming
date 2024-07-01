#!/usr/bin/python3
"""
Class
-----
This represents a rectangle
"""


class Rectangle:
    """
    Attribute
    ---------
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints out the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            symbol = str(getattr(
                self, 'print_symbol', self.__class__.print_symbol))
            return "\n".join([symbol * self.width] * self.height)

    def __repr__(self):
        """Returns a string repr of rect"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Delete rect instace"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Comparing instances and returning the bigger one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.perimeter() > rect_1.perimeter():
            return rect_2
        return rect_1
