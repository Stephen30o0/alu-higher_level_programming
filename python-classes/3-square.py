#!/usr/bin/python3
"""NO MODULES USED IN THIS CODE"""

class Square:
    """Class that defines the sizes of a square
    and gives errors and exceptions"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

 def area(self):
        """Function to return the are of the square"""
        return self.__size ** 2
