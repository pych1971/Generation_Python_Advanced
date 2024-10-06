s = input()
if len(s) == 6:
    print((s[0] + s[-1:-6:-1]).lstrip('0'))
else:
    print(s[-1:-6:-1].lstrip('0'))
