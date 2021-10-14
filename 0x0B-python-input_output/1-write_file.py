#!/usr/bin/python3
'''
1-write_file module
Contains write_file function
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file (UTF8)
    and returns the number of characters written
    '''
    with open(filename, mode='w', encoding='utf-8') as file_1:
        return file_1.write(text)
