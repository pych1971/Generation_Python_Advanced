n, k = int(input()), int(input())
n_list = [i for i in range(1, n + 1)]
while len(n_list) > 1:
    for i in range(1, k):
        tmp = n_list.pop(0)
        n_list.append(tmp)
    n_list.pop(0)
print(*n_list)
