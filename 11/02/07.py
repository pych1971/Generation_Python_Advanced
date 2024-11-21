purchases = {}
for _ in range(int(input())):
    purchase = input().split()
    purchases[purchase[0]] = purchases.get(purchase[0], {})
    purchases[purchase[0]][purchase[1]] = purchases[purchase[0]].get(purchase[1], 0) + int(purchase[2])
for i in sorted(purchases):
    print(f'{i}:')
    for j in sorted(purchases[i]):
        print(f'{j} {purchases[i][j]}')
