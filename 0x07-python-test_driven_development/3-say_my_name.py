#!/usr/bin/python3
'''
3-say_my_name.py module
Functions:
    say_my_name(first_name, last_name=""):
    prints 'my name is' followed by first_name
    and last_name
'''


def say_my_name(first_name, last_name=""):
    '''
    prints 'my name is' followed by first_name
    and last_name
    @first_name: first str
    @last_name: second str
    '''
    err_msg1 = 'first_name must be a string'
    if type(first_name) is not str:
        raise TypeError(err_msg1)

    err_msg2 = 'last_name must be a string'
    if type(last_name) is not str:
        raise TypeError(err_msg2)

    print("My name is {} {}".format(first_name, last_name))
