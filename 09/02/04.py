m, n = int(input()), int(input())
library = {input() for _ in range(m)}
for _ in range(n):
    if input() in library:
        print('YES')
    else:
        print('NO')
