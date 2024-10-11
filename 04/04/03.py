n = int(input())
total = 0
for i in range(n):
    total += list(map(int, input().split()))[i]
print(total)
