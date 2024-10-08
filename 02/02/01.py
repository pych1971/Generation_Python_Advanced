n = int(input())
q1 = q2 = q3 = q4 = 0
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        continue
    if x > 0 and y > 0:
        q1 += 1
    elif x > 0 and y < 0:
        q4 += 1
    elif x < 0 and y > 0:
        q2 += 1
    else:
        q3 += 1
print(f'Первая четверть: {q1}')
print(f'Вторая четверть: {q2}')
print(f'Третья четверть: {q3}')
print(f'Четвертая четверть: {q4}')
