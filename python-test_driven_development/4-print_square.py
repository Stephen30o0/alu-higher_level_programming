#!/usr/bin/python3
"""
prints a square
"""


def print_square(size):
    """
   prints a square using
    Params:
        size – length of square
    Raises:
    TypeError – if size is not an integer,
        or if size is a float and is less than 0
    ValueError – if size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
