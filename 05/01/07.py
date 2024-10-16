field = [['.'] * 8 for _ in range(8)]
knight = input()
x_knight = 8 - int(knight[1])
y_knight = 'abcdefgh'.find(knight[0])
for i in range(8):
    for j in range(8):
        if abs(i - x_knight) == abs(j - y_knight) or i == x_knight or j == y_knight:
            field[i][j] = '*'
field[x_knight][y_knight] = 'Q'
[print(*field[i]) for i in range(8)]
