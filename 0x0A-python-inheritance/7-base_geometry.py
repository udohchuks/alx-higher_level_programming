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
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
