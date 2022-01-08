#!/usr/bin/python3
"""6-peak Python module"""


def find_peak(list_of_integers):
    """Finds the highest peak"""
    if list_of_integers is None or list is []:
        return None
    return max(list_of_integers)
