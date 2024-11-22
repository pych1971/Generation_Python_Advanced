from string import ascii_letters, digits
from random import choice


def generate_password(length):
    password = ''
    symbols = ascii_letters + digits
    for _ in range(length):
        next_symbol = choice(symbols)
        while next_symbol in 'lI1oO0':
            next_symbol = choice(symbols)
        else:
            password += next_symbol
    return password


def generate_passwords(count, length):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
