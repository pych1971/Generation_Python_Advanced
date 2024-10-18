set_numbers = set()
for i in input().split():
    number = int(i)
    if number not in set_numbers:
        print('NO')
        set_numbers.add(number)
    else:
        print('YES')
