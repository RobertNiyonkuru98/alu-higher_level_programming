#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, integer in enumerate(row):
            if i == len(row) - 1:
                print("{}".format(integer))
            else:
                print("{}".format(integer), end=" ")
