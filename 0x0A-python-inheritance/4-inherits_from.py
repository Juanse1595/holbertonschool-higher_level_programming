#!/usr/bin/python3
'''4-inherits_from module'''


def inherits_from(obj, a_class):
    '''
    Returns True if obj is from a subclass of a_class
    '''
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
