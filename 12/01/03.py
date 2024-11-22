import random

length = int(input())  # длина пароля
password = ''
for _ in range(length):
    if random.randint(0, 1):
        password += chr(random.randint(65, 90))
    else:
        password += chr(random.randint(97, 122))
print(password)
