#!/usr/bin/python3
'''0-lookup module'''


def lookup(obj):
    '''
    returns list of attributes and methods of an object
    @obj: object to be analyzed
    '''
    return dir(obj)
