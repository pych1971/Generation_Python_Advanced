n, m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
next_number = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
    print(*matrix[i])
