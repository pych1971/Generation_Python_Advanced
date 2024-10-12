n = int(input())
matrix = []
results = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    arithmetic_mean = sum(matrix[-1]) / n
    total = 0
    for j in range(n):
        if matrix[-1][j] > arithmetic_mean:
            total += 1
    results.append(total)
for i in range(n):
    print(results[i])
