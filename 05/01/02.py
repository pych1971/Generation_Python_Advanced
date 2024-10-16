n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
max_element = -100000000
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j and matrix[i][j] > max_element:
            max_element = matrix[i][j]
print(max_element)
