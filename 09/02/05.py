test1 = {int(i) for i in input().split()}
test2 = {int(i) for i in input().split()}
if test1 & test2 != set():
    print(*sorted(test1 & test2, reverse=True))
else:
    print('BAD DAY')
