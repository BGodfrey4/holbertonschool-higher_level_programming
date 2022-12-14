#!/usr/bin/python3
""" A class Rectangle that defines a rectangle """


class Rectangle:
    """ Class Rectangle
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Will find the width of the rectangle
        Returns:
            width (int): width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Finds the height of the rectangle
        Returns:
            height of rectangle
        """
        return self.__height

    @width.setter
    h(self, value):
        """ Sets the width of the rectangle
        Args:
            value (int): width of
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle
        Args:
            value (int): height of
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Will find the area of the Rectangle
        Returns:
            area (int): area of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Finds the perimeter the Rectangle
        Returns:
            perimeter (int): perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        """ Prints the rectangle
        Returns:
            string: string of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += "#" * self.__width
            if i < self.__height - 1:
                string += "\n"
        return string

    def __print__(self):
        """ Prints the rectangle
        Returns:
            __str__: string of rectangle
        """
    return self.__str__()
