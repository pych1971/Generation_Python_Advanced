from random import randint, shuffle

card = set()
while len(card) < 25:
    card.add(randint(1, 75))
card = list(card)
shuffle(card)
for i in range(5):
    for j in range(5):
        if i == j == 2:
            print(str(0).ljust(3), end='')
        else:
            print(str(card[i * 5 + j]).ljust(3), end='')
    print()
