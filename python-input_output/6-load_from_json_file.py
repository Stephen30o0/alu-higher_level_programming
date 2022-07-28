#!/usr/bin/python3
"""
Module object from a JSON file
"""


import json


def load_from_json_file(filename):
     """creates an Object from a JSON file
    Args:
        filename(str): filename
    Returns:
        returns object created from JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
