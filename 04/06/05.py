n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i + j + 1 == n or i == j:
            matrix[i][j] = 1
    print(*matrix[i])
