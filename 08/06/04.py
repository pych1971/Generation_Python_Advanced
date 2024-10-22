n = int(input())
set_result = set(input())
for i in range(n - 1):
    set_result &= set(input())
print(*sorted(set_result))
