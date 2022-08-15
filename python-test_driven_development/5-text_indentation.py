#!/usr/bin/python3
"""
Module text_indentation
Adds 2 new lines after a certain set characters.
"""


def text_indentation(text):
    """Prints text with added 2 newlines
    after each of these characters ('.', '?', ':').
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in ".:?":
        text = (i + "\n\n").join(
            [line.strip(" ") for line in text.split(i)])

    print("{}".format(text), end="")
