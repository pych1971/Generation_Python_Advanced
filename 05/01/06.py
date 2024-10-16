n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
result = 'YES'
rows = [[i for i in range(1, n + 1)] for j in range(n)]
cols = [[i for i in range(1, n + 1)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] in rows[i] and matrix[i][j] in cols[j]:
            rows[i].remove(matrix[i][j])
            cols[j].remove(matrix[i][j])
        else:
            result = 'NO'
            break
    if result == 'NO':
        break
print(result)
