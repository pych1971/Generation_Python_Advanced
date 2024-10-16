n = int(input())
matrix = []
matrix_tmp = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    matrix_tmp.append([0] * n)
m = int(input())
matrix_res = matrix[:]
while m > 1:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_tmp[i][j] += matrix_res[i][k] * matrix[k][j]
    matrix_res = matrix_tmp[:]
    matrix_tmp = [[0 for i in range(n)] for j in range(n)]
    m -= 1
for i in range(n):
    print(*matrix_res[i])
