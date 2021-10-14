#!/usr/bin/python3
'''
2-append_write module
Contains append_write function
'''


def append_write(filename="", text=""):
    '''
    appends a string at the end of a text file
    @filename: file
    @text: text to be appended to the file filename
    '''
    with open(filename, mode='a', encoding='utf-8') as file_1:
        return file_1.write(text)
