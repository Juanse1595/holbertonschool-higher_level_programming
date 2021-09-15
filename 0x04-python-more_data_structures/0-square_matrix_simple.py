#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in row] for row in matrix]
    return new_matrix


'''
    new_matrix = []
    for row in matrix:
        sublist = []
        for num in row:
            sublist.append(num ** 2)
        new_matrix.append(sublist)
    return new_matrix
'''
