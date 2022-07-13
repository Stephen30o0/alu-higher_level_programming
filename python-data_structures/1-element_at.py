#!/usr/bin/python3
#function that retrieves an element from a list like in C
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    elif idx >= len(my_list):
        return "None"
    else:
        return print(f"Element at index {idx} is {my_list[idx]}")
