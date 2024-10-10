n = int(input())
for i in range(n):
    rif = input()
    look_for = 'anton'
    for j in rif:
        if j == look_for[0]:
            look_for = look_for[1:]
            if look_for == '':
                print(i + 1, end=' ')
                break
