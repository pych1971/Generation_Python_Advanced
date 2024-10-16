n, m = map(int, input().split())
matrix = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'
    print(*matrix[i])
