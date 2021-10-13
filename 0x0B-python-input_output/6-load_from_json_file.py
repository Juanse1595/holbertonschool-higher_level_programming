#!/usr/bin/python3
'''
6-load_from_json_file module
Contains load_from_json_file function
'''
import json


def load_from_json_file(filename):
    '''
    Creates an Object from a “JSON file”
    '''
    with open(filename) as file_1:
        return json.load(file_1)
