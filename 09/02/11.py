m = int(input())
full_list = []
for i in range(m):
    n = int(input())
    full_list.append({input() for _ in range(n)})
result = full_list[0]
for i in range(1, m):
    result &= full_list[i]
print(*sorted(result), sep='\n')
