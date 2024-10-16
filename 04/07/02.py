matrix1 = []
matrix2 = []
n, m = map(int, input().split())
for i in range(n):
    matrix1.append(list(map(int, input().split())))
_ = input()
m, k = map(int, input().split())
for i in range(m):
    matrix2.append(list(map(int, input().split())))
matrix_com = [[0] * n for i in range(k)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            matrix_com[i][j] += matrix1[i][x] * matrix2[x][j]
    print(*matrix_com[i])
