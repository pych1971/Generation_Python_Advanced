result = {}
for i in input().split():
    result[i] = result.get(i, 0) + 1
    print(result[i], end=' ')
