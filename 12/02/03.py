from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
new_matrix = []
for i in matrix:
    new_matrix += i
shuffle(new_matrix)
for i in range(4):
    for j in range(4):
        matrix[i][j] = new_matrix[i * 4 + j]
