#!/usr/bin/python3
class Square:
    """Private instance attribute: size:
    property def size(self)
    property setter def size(self, value)
    """

    def __init__(self, size=0):
        """Initializes the data."""
        self.square_size = size

    @property
    def size(self):
        """gets the size of the square
        and returns it."""
        return self.square_size

     @size.setter
    def size(self, value):
        """sets the size of the value
            raises Type and Value error if its not an interger
            and is less than zeo repectively"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
