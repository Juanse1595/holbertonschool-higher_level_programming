#!/usr/bin/python3
'''
2-is_same_class module
contains is_same_class method
'''


def is_same_class(obj, a_class):
    '''
    returns True if the class of obj is the same a_class
    '''
    return (type(obj) is a_class)
