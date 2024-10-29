t9 = {'1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ',
      '0': ' '}
for i in input().upper():
    for j in t9.keys():
        if i in t9[j]:
            print(j * (t9[j].index(i) + 1), end='')
