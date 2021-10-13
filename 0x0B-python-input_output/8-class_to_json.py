#!/usr/bin/python3
'''8-class_to_json module'''


def class_to_json(obj):
    '''
    Returns the dictionary description of an object
    '''
    return obj.__dict__
