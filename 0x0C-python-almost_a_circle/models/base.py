#!/usr/bin/python3
'''
models/base.py module
Contains
    Class:
    1. Base
'''


class Base:
    '''
    Contains:
        Fields:
        __nb_objects

        Methods:
        __init__
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
