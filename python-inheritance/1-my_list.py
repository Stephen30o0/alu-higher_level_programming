#!/usr/bin/python3
"""
No modules
"""


class MyList(list):
    """creates a subclass Mylist of superclass list"""
    def print_sorted(self):
        """print sorted list"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
