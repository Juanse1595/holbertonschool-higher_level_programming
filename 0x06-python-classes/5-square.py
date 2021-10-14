#!/usr/bin/python3
'''Defining a Square class'''


class Square:
    '''
    Square class

    Attributes:
        size (int): size of the Square
    '''
    def __init__(self, size=0):
        '''
        Initialize square

        Attributes:
            size (int): size of square
        '''
        self.size = size

    @property
    def size(self):
        '''
        Gets size of Square

        Return: size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the size to value

        Attributes:
            size: size of the Square
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns the area of the square

        Returns:
            area of square
        '''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square in stdout'''
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for y in range(1, self.__size):
                    print("#", end="")
                print("#")
