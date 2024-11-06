state = []
for _ in range(int(input())):
    state.append(input().split())
for _ in range(int(input())):
    city = input()
    for i in state:
        if city in i:
            print(i[0])
            break
