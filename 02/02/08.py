tim, rus = input(), input()
positions = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
if tim == rus:
    print('ничья')
elif abs(positions.index(tim) - positions.index(rus)) % 2 == 0 and positions.index(tim) > positions.index(rus) or abs(
        positions.index(tim) - positions.index(rus)) % 2 != 0 and positions.index(tim) < positions.index(rus):
    print('Тимур')
else:
    print('Руслан')
