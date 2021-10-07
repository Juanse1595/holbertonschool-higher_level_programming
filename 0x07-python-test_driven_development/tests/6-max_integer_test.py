#!/usr/bin/python3
'''
6-max_integer unittest
test if the max_integer function works correctly
'''


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''contains all the test cases'''

    def test_max(self):
        '''test corrent result'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([42, -122, 30]), 42)

    def test_type(self):
        '''test correct error'''
        self.assertRaises(TypeError, max_integer, ['hi', 2])
        self.assertRaises(TypeError, max_integer, [1.2, 5.89, ()])
