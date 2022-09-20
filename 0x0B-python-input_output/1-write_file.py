#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""


def write_file(filename="", text=""):
    """Will write the text in filename.

    Args:
        - filename: is the name of the file
        - text: is the string writtin in the file

    Returns: is the number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)
