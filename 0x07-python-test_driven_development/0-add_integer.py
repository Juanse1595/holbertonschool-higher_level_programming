#!/usr/bin/python3
'''
0-add_integer module
Contains:
    add_integer: adds 2 integers
'''


def add_integer(a, b=98):
    '''
    adds two integers or floats
    @a: first integer
    @b: second integer
    a and b must be casted to integers if they're floats
    Returns: integer, the addition of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
