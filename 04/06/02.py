n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i > n - 1 - j:
            matrix[i][j] = 2
    print(*matrix[i])
