#!/usr/bin/python3
"""Module 3-to_json_string.
Will return the JSON representation of the object.
"""


import json


def to_json_string(my_obj):
    """Will return th JSON representation of my_obj.

    Args:
        - my_obj: is the string represented

    Returns: is just the JSON representation
    """

    return json.dumps(my_obj)
