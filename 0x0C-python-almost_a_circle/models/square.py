#!/usr/bin/python3
""" a square module that is inherited from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherited from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """retrieving size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting value to the size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
