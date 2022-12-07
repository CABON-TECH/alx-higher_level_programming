#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = [[] for x in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sq_matrix[i].append(matrix[i][j] ** 2)

    return sq_matrix
