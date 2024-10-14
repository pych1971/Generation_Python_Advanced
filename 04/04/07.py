matrix = []
n = int(input())
sum_up = sum_down = sum_right = sum_left = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if i < j and i < n - 1 - j:
            sum_up += matrix[i][j]
        elif i < j and i > n - 1 - j:
            sum_right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            sum_down += matrix[i][j]
        elif i > j and i < n - 1 - j:
            sum_left += matrix[i][j]
print(f'Верхняя четверть: {sum_up}')
print(f'Правая четверть: {sum_right}')
print(f'Нижняя четверть: {sum_down}')
print(f'Левая четверть: {sum_left}')
