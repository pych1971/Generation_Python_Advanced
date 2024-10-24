m, n = int(input()), int(input())
pupils = len({input() for i in range(m)} ^ {input() for j in range(n)})
if pupils == 0:
    print('NO')
else:
    print(pupils)
