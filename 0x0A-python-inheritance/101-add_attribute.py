#!/usr/bin/python3
'''101 module'''


def add_attribute(self, attr, value):
    '''try to add attribute'''
    return_get = getattr(self, '__slots__', "noup")
    if return_get != "noup":
        raise TypeError("can't add new attribute")
    setattr(self, attr, value)
    
