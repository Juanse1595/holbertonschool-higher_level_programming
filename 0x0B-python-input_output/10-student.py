#!/usr/bin/python3
'''10-student module'''


class Student:
    '''
    Attr:
        first_name
        last_name
        age
    Methods:
        __init__
        to_json
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = dict()
        try:
            for attr in attrs:
                if attr in self.__dict__.keys():
                    my_dict[attr] = self.__dict__[attr]
            return my_dict
        except TypeError:
            return self.__dict__
