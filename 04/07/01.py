n, m = map(int, input().split())
matrix1 = []
matrix2 = []
matrix_sum = [[0] * m for i in range(n)]
for i in range(n):
    matrix1.append(list(map(int, input().split())))
_ = input()
for i in range(n):
    matrix2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j]
    print(*matrix_sum[i])
