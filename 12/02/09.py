from random import choice, shuffle


def generate_password(length):
    password = ''
    symbols = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    password += choice('ABCDEFGHJKLMNPQRSTUVWXYZ') + choice('abcdefghijkmnpqrstuvwxyz') + choice('23456789')
    while len(password) < length:
        password += choice(symbols)
    password = list(password)
    shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
