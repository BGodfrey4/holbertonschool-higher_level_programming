#!/usr/bin/python3
"""A simple Square class that specifies a square by the size."""


class Square:
    """A simple Square class that specifies the square by the size.

    Attributes:
        __size (int): Is the size of the square.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size is always an integer")
        if size < 0:
            raise ValueError("size is always >= 0")
        self.__size = size

    def area(self):
        """Will find the area of the square.

        Returns:
            int : Is just the area of the square.
        """
        return self.__size ** 2
