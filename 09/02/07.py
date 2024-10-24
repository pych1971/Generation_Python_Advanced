m, n = int(input()), int(input())
print(len({input() for i in range(m)} - {input() for j in range(n)}))
