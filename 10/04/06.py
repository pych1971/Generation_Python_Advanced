phones = {}
for _ in range(int(input())):
    phone, name = input().split()
    phones[name.lower()] = phones.get(name.lower(), [])
    phones[name.lower()].append(phone)
for _ in range(int(input())):
    name = input().lower()
    if name in phones.keys():
        print(*phones[name])
    else:
        print('абонент не найден')
