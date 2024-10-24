n = int(input())
cities = {input() for _ in range(n)}
if input() in cities:
    print('REPEAT')
else:
    print('OK')
