#!/usr/bin/python3
"""Module 0-read_file.
Will read from the file and print.
"""


def read_file(filename=""):
    """Will read from filename and print
    its contents to stdout.
    Args:
        - filename: is the name of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
