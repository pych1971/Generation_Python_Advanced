result = {}
for i in input().split():
    result[i] = result.get(i, 0) + 1
    if result[i] > 1:
        print(f'{i}_{result[i] - 1}', end=' ')
    else:
        print(i, end=' ')
