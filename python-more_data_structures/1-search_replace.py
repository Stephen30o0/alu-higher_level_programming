#!/usr/bin/python3
def search_replace(my_list, search, replace):
    00_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            00_list[i] = replace
    return 00_list
