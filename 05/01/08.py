n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)
    print(*matrix[i])
