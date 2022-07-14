#!/usr/bin/python3
def no_c(my_string):
    replace = ''
    for i in my_string:
        if (i.lower()) == 'c':
            continue
        replace += i
    return replace
