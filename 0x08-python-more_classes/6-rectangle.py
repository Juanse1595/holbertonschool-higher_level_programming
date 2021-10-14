#!/usr/bin/python3
'''
2-square module
class Rectangle
with height and width attributes
area and perimeter methods
__str__ method
__repr__ method
__del__ method
number_of_instances class attribute
'''


class Rectangle:
    '''
    class Rectangle
    Init of 2 attributes:
        Width
        Height
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height - 1):
            string += ("#" * self.__width) + "\n"
        string += ("#" * self.__width)
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
