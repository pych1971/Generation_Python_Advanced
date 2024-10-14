n = int(input())
matrix = []
new_matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    new_matrix.append([0] * n)
for i in range(n):
    for j in range(n):
        new_matrix[i][j] = matrix[n - j - 1][i]
    print(*new_matrix[i])
