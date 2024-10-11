n = int(input())
new_list = []
for i in range(n):
    new_list.append([i for i in range(1, n + 1)])
    print(new_list[i])
