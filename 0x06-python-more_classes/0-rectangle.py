#!/usr/bin/python3
"""Will write the class that defines a
rectangle by width and height
"""


class Rectangle:
    """Is the rectangle class defined by the width and height.
    """

    def __init__(self, width=0, height=0):
        """Will initialize the weight and height attributes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Will retrieve the width of the Rectangle instance
        """
        return self.__width

    @property
    def height(self):
        """Will retrieve the height of the Rectangle instance
        """
        return self.__height

    @width.setter
    def width(self, value):
        """will set the width of a rectangle instance
        """
        if type(value) is not int:
            raise TypeError("the width must be an integer")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Will set the height of a Rectangle instance
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
