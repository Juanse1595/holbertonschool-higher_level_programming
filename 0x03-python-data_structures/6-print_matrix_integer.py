#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        count = 0
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end="")
                if count < (len(row) - 1):
                    print(" ", end="")
                count += 1
            print()
            count = 0
