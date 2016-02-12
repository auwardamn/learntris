from __future__ import print_function

def create_empty_matrix(m, n):
    """Returns an mxn empty (.) matrix"""
    matrix = []
    for i in range(0, n):
        row = []
        for i in range(0, m):
            row.append('.')
        matrix.append(row)
    return matrix

def clear_row(matrix, row_num):
    """Returns Matrix with requested row cleared"""
    width = len(matrix[1])
    matrix[row_num] = []
    for i in range(0, width):  # Do as many times as items per row
        matrix[row_num].append('.')
    return matrix

def print_matrix(matrix):
    """prints provided matrix of seperate elements to the screen with " " seperation"""
    for i in range(0, len(matrix)):  # For Each row of the matrix
        print(*matrix[i], sep=" ")  # Print Each item of current row with " " seperation