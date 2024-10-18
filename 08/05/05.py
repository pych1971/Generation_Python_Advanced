n = int(input())
names = set()
corrects = 0
for _ in range(n):
    name, result = input().split(':')
    if result == ' Correct':
        names.add(name)
        corrects += 1
if corrects > 0:
    print(f'Верно решили {len(names)} учащихся')
    print(f'Из всех попыток {int(corrects / n * 100 + 0.5)}% верных')
else:
    print('Вы можете стать первым, кто решит эту задачу')
