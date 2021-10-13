#!/usr/bin/python3
'''101 module'''


def add_attribute(self, attr, value):
    '''try to add attribute'''
    if not ('__dict__' in dir(self)):
        raise TypeError("can't add new attribute")
    setattr(self, attr, value)
