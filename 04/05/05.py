n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
for j in range(n):
    matrix[j][j], matrix[n - j - 1][j] = matrix[n - j - 1][j], matrix[j][j]
for i in range(n):
    print(*matrix[i])
