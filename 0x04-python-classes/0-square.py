#!/usr/bin/python3
"""A simple Square class specifies a square by the size."""


class Square:
    """A simple Square class that specifies a square by the size.
    Attributes:
        __size (int): Is the size of the square.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
