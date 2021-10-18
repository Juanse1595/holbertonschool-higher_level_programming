#!/usr/bin/python3
'''
models/base.py module
Contains
    Class:
    1. Base
'''
import json


class Base:
    '''
    Contains:
        Fields:
        __nb_objects

        Methods:
        __init__
        to_json_string
        save_to_file
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is {}:
            return '[]'
        return json.dumps(list_dictionaries)
