from random import choice

pupils = []
for _ in range(int(input())):
    pupils.append(input())
friends = pupils[:]
for pupil in pupils:
    print(f'{pupil} - ', end='')
    friend = choice(friends)
    while friend == pupil:
        friend = choice(friends)
    else:
        print(friend)
        friends.remove(friend)
