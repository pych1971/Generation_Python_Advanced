symbols = input().split()
new_list = [[]]
for i in range(1, len(symbols) + 1):
    for j in range(0, len(symbols) - i + 1):
        new_list.append(symbols[j:j + i])
print(new_list)
