#!/usr/bin/python3
"""
Square object inherits from Rectangle object
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str___"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to dictionary"""
        return({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            })
