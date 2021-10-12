#!/usr/bin/python3
'''
3-to_json_string module
Contains to_json_string function
'''
import json


def to_json_string(my_obj):
    '''
    returns the JSON representation of an object (string)
    '''
    return json.dumps(my_obj)
