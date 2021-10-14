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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
