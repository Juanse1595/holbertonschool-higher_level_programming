#!/usr/bin/python3
'''
1-my_lyst module
Contains class MyList
'''


class MyList(list):
    '''
    class MyList
    Contains print_sorted method
    '''
    def print_sorted(self):
        '''
        prints an ordered list
        '''
        print(sorted(self))
