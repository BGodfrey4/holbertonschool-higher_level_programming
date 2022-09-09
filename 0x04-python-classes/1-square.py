#!/usr/bin/python3
""" will write the class square"""


class Square:
    """will attempt to model the square"""

    def __init__(self, size=0):  # then the instantiation happens here
        if type(size) != int:
            raise TypeError("is just the size must be an integer")
        if size < 0:
            raise ValueError("is the size must be >= 0")
        self.__size = size
