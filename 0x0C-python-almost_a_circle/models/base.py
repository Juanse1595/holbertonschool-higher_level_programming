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
        '''instantation of object'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return json representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries is {}:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        save in a file the json
        representation of list_objs
        '''
        if list_objs is None:
            list_objs = []
        instances_dict = []
        for instance in list_objs:
            instances_dict.append((instance.to_dictionary()).copy())
        json_dict = Base.to_json_string(instances_dict)
        with open('{}.json'.format(cls.__name__), mode='w') as file_1:
            file_1.write(json_dict)
