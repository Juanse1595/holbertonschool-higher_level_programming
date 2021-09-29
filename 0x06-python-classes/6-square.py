#!/usr/bin/python3
'''Defining a Square class'''


class Square:
    '''
    Square class

    Attributes:
        size (int): size of the Square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize square

        Attributes:
            size (int): size of square
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''
        Gets position of square

        Return: position
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Returns the area of the square

        Returns:
            area of square
        '''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square in stdout'''
        if self.__size == 0:
            print("")
        else:
            for blanck_row in range(self.__position[1]):
                print("")
            for row in range(0, self.__size):
                for blank_column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(1, self.__size):
                    print("#", end="")
                print("#")
