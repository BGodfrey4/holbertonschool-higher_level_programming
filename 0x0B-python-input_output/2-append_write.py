#!/usr/bin/python3
"""Module 4-append_write.
Will append the string at the end of the text file.
"""


def append_write(filename="", text=""):
    """Will append the text to filename.

    Args:
        - filename: is just the name of the file
        - text: is just the text to append

    Returns: is just the number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
