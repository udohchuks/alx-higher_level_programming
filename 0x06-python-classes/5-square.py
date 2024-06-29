#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    Represent a square

    Attributes:
      size: size
    """
    def __init__(self, size=0):
        """
        Init object

        Args:
          size: size
        Raise:
          TypeError: if size not an int
          ValueError: if size less than 1
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")

    @property
    def size(self):
        """
        Return size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square
        """
        for _ in range(self.__size):
            if self.__size == 0:
                print()
            else:
                print("#" * self.__size)
