matrix = []
max_element = -100000000000
n = int(input())
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if (i >= j and i <= n - 1 - j or i <= j and i >= n - 1 - j) and matrix[i][j] > max_element:
            max_element = matrix[i][j]
print(max_element)
