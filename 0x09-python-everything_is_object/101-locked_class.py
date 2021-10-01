#!/usr/bin/python3
'''101-locked_class'''


class LockedClass():
    '''class LockedClass
    no new attributes can be created
    only first_name
    '''
    __slots__ = "first_name"
