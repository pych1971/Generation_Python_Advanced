n = int(input())
matrix = []
result = 'YES'
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break
print(result)
