#!/usr/bin/python3
'''
0-read_file module
contains read_file function
'''


def read_file(filename=""):
    '''
    opens a file and read the content, UTP8 format
    '''
    with open(filename, encoding='utf-8') as file_1:
        print(file_1.read(), end='')
