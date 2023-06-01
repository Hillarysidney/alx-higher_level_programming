#!/usr/bin/python3
"""Create a Class Square"""


class Square:
    """This is aClass Square"""

    def __init__(self, size=0):
        """Stating of a Square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def __lt__(self, other):
        """equating operator <"""
        return (self.area() < other.area())

    def __le__(self, other):
        """equating operator <="""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """equating operator >"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """equating operator >="""
        return (self.area() >= other.area())

    def __eq__(self, other):
        """equating operator =="""
        return (self.area() == other.area())

    def __ne__(self, other):
        """equating operator !="""
        return (self.area() != other.area())

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of attribute size private"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the attribute size"""
        if ((type(value) is int) or (type(value) is float)):
            if (value < 0):
                raise (ValueError("size must be >= 0"))
            else:
                self.__size = value
        else:
            raise (TypeError("size must be a number"))
