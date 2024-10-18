n = int(input())
unique_symbols = []
for i in range(n):
    unique_symbols.append(len(set(input().lower())))
print(*unique_symbols, sep='\n')
