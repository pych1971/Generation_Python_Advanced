n, m = map(int, input().split())
a = []
x = 0
y = -1
i = 1
hor = 0
ver = 1
for j in range(n):
    a.append([0] * m)
while i <= n * m:
    if 0 <= x + hor < n and 0 <= y + ver < m and a[x + hor][y + ver] == 0:
        x += hor
        y += ver
        a[x][y] = i
        i += 1
    else:
        if ver == 1:
            ver = 0
            hor = 1
        elif hor == 1:
            hor = 0
            ver = -1
        elif ver == -1:
            ver = 0
            hor = -1
        elif hor == -1:
            hor = 0
            ver = 1
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
