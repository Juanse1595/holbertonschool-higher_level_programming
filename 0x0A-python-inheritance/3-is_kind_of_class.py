#!/usr/bin/python3
'''
3-is_kind_of_class module
'''


def is_kind_of_class(obj, a_class):
    '''
    returns True if obj is instance of a_class or parent
    class
    '''
    return isinstance(obj, a_class)
