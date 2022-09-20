#!/usr/bin/python3
"""Module 5-save_to_json_file.
Will write an Object to a text file,
that uses the JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Will write the representation of my_obj
    to the filename.

    Args:
        - my_obj: is the object to be written
        - filename: is the file written into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
