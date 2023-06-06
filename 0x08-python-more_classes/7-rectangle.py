#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Start a rectangle.
    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """For a new Rectangle.
        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting and setting the width of the Rectangle."""
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
        """Getting and setting the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangles = []
        for o in range(self.__height):
            [rectangles.append(str(self.print_symbol)) for j in range(self.__width)]
            if o != self.__height - 1:
                rectangles.append("\n")
        return ("".join(rectangles))

    def __repr__(self):
        """Returns string representation of the Rectangle."""
        rectangles = "Rectangle(" + str(self.__width)
        rectangles += ", " + str(self.__height) + ")"
        return (rectangles)

    def __del__(self):
        """Print a message in every deletion of the Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
