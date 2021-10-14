#!/usr/bin/python3
'''
4-print_square module
Functions:
    print_square(size):
    prints a square with the '#' char
'''


def print_square(size):
    '''
    prints a square with the '#' char
    @size: size of the square
    size must be an int
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    row = '#' * size
    for idx in range(size):
        print(row)
