n = int(input())
matrix = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i == n // 2 or j == n // 2 or i + j + 1 == n:
            matrix[i][j] = '*'
    print(*matrix[i])
