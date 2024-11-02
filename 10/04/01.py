dictionary = {}
for i in range(int(input())):
    key, value = input().split(':')
    dictionary[key.lower()] = value[1:]
for i in range(int(input())):
    term = input()
    if term.lower() not in dictionary:
        print('Не найдено')
    else:
        print(dictionary[term.lower()])
