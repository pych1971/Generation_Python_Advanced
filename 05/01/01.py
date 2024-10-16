l = list(input().split())
n = int(input())
new_list = [[] for i in range(n)]
for i in range(n):
    new_list[i] = l[i::n]
print(new_list)
