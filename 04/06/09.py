n, m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
next_number = 1
for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = next_number
                next_number += 1
for i in range(n):
    print(*matrix[i])
