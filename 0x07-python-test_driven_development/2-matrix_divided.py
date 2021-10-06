#!/usr/bin/python3
'''
2-matrix_divided module
Functions:
    matrix_divided(matrix, div):
    Divides all elements of matrix by div
'''


def matrix_divided(matrix, div):
    '''
    divides each row of matrix by div
    @matrix: given matrix
    @div: divider of each element of the rows of 
    matrix
    Returns a new matrix with the result
    '''
    err_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(element, (int, float)) for row
        in matrix for element in row):
        raise TypeError(err_msg1)

    err_msg2 = "Each row of the matrix must have the same size"
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError(err_msg2)

    err_msg3 = "div must be a number"
    if not isinstance(div, (int, float)):
        raise TypeError(err_msg3)

    new_matrix = [[round((element / div), 2) for element in row] \
                 for row in matrix]
    return new_matrix

