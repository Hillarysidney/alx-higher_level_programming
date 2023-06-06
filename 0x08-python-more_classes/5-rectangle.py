#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """rectangle."""

    def __init__(self, width=0, height=0):
        """Start a new Rectangle.
        Args:
            width (int): The Width of the new rectangle.
            height (int): A Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting and setting of width of the Rectangle."""
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
        """Getting and setting of height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns of area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns of perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns of printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangles = []
        for o in range(self.__height):
            [rectangles.append('#') for j in range(self.__width)]
            if o != self.__height - 1:
                rectangles.append("\n")
        return ("".join(rectangles))

    def __repr__(self):
        """Returns of string representation of the Rectangle."""
        rectangles = "Rectangle(" + str(self.__width)
        rectangles += ", " + str(self.__height) + ")"
        return (rectangles)

    def __del__(self):
        """Print message in every deletion of the Rectangle."""
        print("Bye rectangle...")
