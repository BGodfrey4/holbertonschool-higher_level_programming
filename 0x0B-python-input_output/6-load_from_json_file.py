#!/usr/bin/python3
"""Module 6-load_from_json_file.
Will create an object from the “JSON file”.
"""


import json


def load_from_json_file(filename):
    """Will create the object from filename.

    Args:
        - filename: is the name of the JSON file

    Returns: is just the object
    """

    with open(filename, 'r') as f:
        return json.load(f)
