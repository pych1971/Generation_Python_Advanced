n = int(input())
matrix = []
magic_square = 'YES'
for i in range(n):
    matrix.append(list(map(int, input().split())))
test_numbers = [i for i in range(1, n ** 2 + 1)]
sum_diag = 0
sum_diag_spare = 0
sum_hor = [0] * n
sum_ver = [0] * n
for i in range(n):
    sum_hor[i] = sum(matrix[i])
    for j in range(n):
        sum_ver[j] += matrix[i][j]
        if matrix[i][j] not in test_numbers:
            magic_square = 'NO'
            break
        else:
            test_numbers.remove(matrix[i][j])
        if i == j:
            sum_diag += matrix[i][j]
        if i + j + 1 == n:
            sum_diag_spare += matrix[i][j]
    if magic_square == 'NO':
        break
for i in range(n):
    for j in range(n):
        if sum_hor[i] == sum_ver[j] == sum_diag == sum_diag_spare:
            continue
        else:
            magic_square = 'NO'
            break
    if magic_square == 'NO':
        break
print(magic_square)
