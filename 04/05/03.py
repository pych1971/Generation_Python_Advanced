n, m = int(input()), int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
y1, y2 = list(map(int, input().split()))
for i in range(n):
    matrix[i][y1], matrix[i][y2] = matrix[i][y2], matrix[i][y1]
    print(*matrix[i])
