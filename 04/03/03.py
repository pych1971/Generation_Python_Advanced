def pascal(n):
    triangle = []
    for i in range(n + 1):
        triangle.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    return triangle[n]


print(pascal(int(input())))
