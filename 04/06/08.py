n, m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
next_number = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = next_number
            next_number += 1
    else:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = next_number
            next_number += 1
    print(*matrix[i])
