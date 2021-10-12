#!/usr/bin/python3
'''100-my_int module'''


class MyInt(int):
    '''
    modify __eq__ and __ne__ methods
    '''
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return (self.value is not other)

    def __ne__(self, other):
        return (self.value is other)
