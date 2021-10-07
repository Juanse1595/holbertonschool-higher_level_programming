#!/usr/bin/python3
'''
5-text_indentation module
Functions:
    text_indentation(text):
    prints a text, for each of this chars ('?', '.', ':')
    that part of the text is followed by two new lines
'''

def text_indentation(text):
    '''
    prints a text, for each of this chars ('?', '.', ':')
    that part of the text is followed by two new lines
    @text: text to be printed
    text must be a str
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')

    delim = ('?', '.', ':')
    i = 0
    text_len = len(text)
    while i < text_len:
        if i == 0 and text[i] == " ":
            while i < text_len and text[i] == " ":
                i += 1
        elif text[i] in delim:
            print('{}\n'.format(text[i]))
            i += 1
            while i < text_len and text[i] == " ":
                i += 1
        else:
            print(text[i], end='')
            i += 1
