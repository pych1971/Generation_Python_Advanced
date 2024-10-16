n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
symmetry = 'YES'
for i in range(n - 1):
    for j in range(i, n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            symmetry = 'NO'
            break
    if symmetry == 'NO':
        break
print(symmetry)
