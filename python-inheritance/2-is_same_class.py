#!/usr/bin/python3
"""
No Modules
"""


def is_same_class(obj, a_class):
    """Function to determine if obj is an instance of a_class.
    Args:
        obj(obj): object
        a_class(class): class
    Return:
        True: if it is an instance of the given class
        False: if not an instance of given class
    """

    if type(obj) is a_class:
        return True
    return False
