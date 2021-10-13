#!/usr/bin/python3
'''
5-save_to_json_file module
Contains save_to_json_file function
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Returns an object (Python data structure)
    represented by a JSON string
    '''
    with open(filename, mode='w') as file_1
        return json.dump(my_obj, file_1)
