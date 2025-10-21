# Transpose a matrix in Python
transpose_matrix = lambda m: [list(row) for row in zip(*m)]
print(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))  # Output: [[1, 3, 5], [2, 4, 6]]

# Transpose a matrix using map and zip
def transpose_matrix_map_zip(m):
    return list(map(list, zip(*m)))
print(transpose_matrix_map_zip([[1, 2, 3], [4, 5, 6]]))  # Output: [[1, 4], [2, 5], [3, 6]]
print(transpose_matrix_map_zip([[7, 8], [9, 10], [11, 12]]))  # Output: [[7, 9, 11], [8, 10, 12]]


# Transpose a matrix using list comprehension
def transpose_matrix_comp(m):
    return [[m[j][i] for j in range(len(m))] for i in range
(len(m[0]))]
print(transpose_matrix_comp([[1, 2, 3], [4, 5, 6]]))  # Output: [[1, 4], [2, 5], [3, 6]]
print(transpose_matrix_comp([[7, 8], [9, 10], [11, 12]]))  # Output: [[7, 9, 11], [8, 10, 12]]


# Transpose a matrix using numpy
import numpy as np
def transpose_matrix_numpy(m):
    return np.array(m).T.tolist()
print(transpose_matrix_numpy([[1, 2], [3, 4], [5, 6]]))  # Output: [[1, 3, 5], [2, 4, 6]]
print(transpose_matrix_numpy([[10, 20, 30], [40, 50, 60]]))  # Output: [[10, 40], [20, 50], [30, 60]]


# Transpose a square matrix in place
def transpose_square_matrix_in_place(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m
print(transpose_square_matrix_in_place([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(transpose_square_matrix_in_place([[10, 20], [30, 40]]))  # Output: [[10, 30], [20, 40]]


# Transpose a matrix using for loops
def transpose_matrix_for_loops(m):
    transposed = []
    for i in range(len(m[0])):
        new_row = []
        for j in range(len(m)):
            new_row.append(m[j][i])
        transposed.append(new_row)
    return transposed   
print(transpose_matrix_for_loops([[1, 2], [3, 4], [5, 6]]))  # Output: [[1, 3, 5], [2, 4, 6]]
print(transpose_matrix_for_loops([[7, 8, 9], [10, 11, 12]]))  # Output: [[7, 10], [8, 11], [9, 12]]