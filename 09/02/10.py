m, n = int(input()), int(input())
pupils = [input() for i in range(m + n)]
result = m + n - (len(pupils) - len(set(pupils))) * 2
if result == 0:
    print('NO')
else:
    print(result)
