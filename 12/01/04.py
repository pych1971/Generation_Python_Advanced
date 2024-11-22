import random

lottery = set()
while len(lottery) < 7:
    lottery.add(random.randint(1, 49))
print(*sorted(lottery))
