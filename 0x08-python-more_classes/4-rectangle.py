#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """rectangle."""

    def __init__(self, width=0, height=0):
        """Settings a new Rectangle.
        Args:
            width (int): Width of the new rectangle.
            height (int): Weight of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting and setting of the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting and setting of the the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangular = []
        for t in range(self.__height):
            [rectangular.append('#') for j in range(self.__width)]
            if t != self.__height - 1:
                rectangular.append("\n")
        return ("".join(rectangular))

    def __repr__(self):
        """returns string representation of the Rectangle."""
        rectangular = "Rectangle(" + str(self.__width)
        rectangular += ", " + str(self.__height) + ")"
        return (rectangular)
