#!/usr/bin/python3
"""NO MODULES USED IN THIS CODE"""


class Square:
    """Class that defines the sizes of a square
    and gives errors and exceptions
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.square_size = size

    def area(self):
        """Function to return the are of the square"""
        return self.square_size ** 2

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

     def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()

