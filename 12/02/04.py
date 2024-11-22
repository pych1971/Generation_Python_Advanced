from random import randint

lottery = set()
while len(lottery) < 100:
    lottery.add(randint(1000000, 9999999))
[print(ticket) for ticket in lottery]
