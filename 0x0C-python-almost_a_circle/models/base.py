#!/usr/bin/python3
"""
Module models.base
This module contains the Base class
"""


class Base:
    """
    Base class for managing id attribute in all future classes.

    Attributes:
    __nb_objects (int): Private class attribute
    id (int): Public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
        id (int, optional): The ID value to be assigned to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
