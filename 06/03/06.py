n = int(input())
pupils = []
for _ in range(n):
    pupils.append(input())
for i in pupils:
    print(i)
print()
for i in pupils:
    if int(i[-1]) >= 4:
        print(i)
