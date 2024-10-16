n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
matrix_trans = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix_trans[i][j] = matrix[j][i]
    print(*matrix_trans[i])
