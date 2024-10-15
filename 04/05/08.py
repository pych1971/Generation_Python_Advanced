field = [['.'] * 8 for _ in range(8)]
knight = input()
x_knight = 8 - int(knight[1])
y_knight = 'abcdefgh'.find(knight[0])
field[x_knight][y_knight] = 'N'
for i in range(8):
    for j in range(8):
        if (abs(i - x_knight) == 1 and abs(j - y_knight) == 2 or abs(i - x_knight) == 2 and abs(
                j - y_knight) == 1) and 0 <= i <= 7 and 0 <= j <= 7:
            field[i][j] = '*'
[print(*field[i]) for i in range(8)]
