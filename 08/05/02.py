n = int(input())
unique_symbols = []
s = ''
sum_symbols = 0
for _ in range(n):
    s += input().lower()
print(len(set(s)))
