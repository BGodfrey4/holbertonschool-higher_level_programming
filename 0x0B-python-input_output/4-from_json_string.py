#!/usr/bin/python3
"""Module 4-from_json_string.
Will return an object (Python data structure)
thats represented by the JSON string.
"""


import json


def from_json_string(my_str):
    """Will return the object thats represented by my_str.
    Args:

        - my_str: is the JSON string representation
    Returns: is the corresponding object
    """

    return json.loads(my_str)
