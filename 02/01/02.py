mass, height = float(input()), float(input())
idx = mass / height ** 2
if idx < 18.5:
    print('Недостаточная масса')
elif idx > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
