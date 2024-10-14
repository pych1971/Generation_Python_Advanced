n = int(input())
matrix = []
for i in range(n):
    matrix.append(input())
for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
for i in range(n):
    print(matrix[i])
