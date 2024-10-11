n = int(input())
new_list = []
for i in range(n):
    new_list.append([j for j in range(1, i + 2)])
    print(new_list[i])
