s = input()
s_new = ''
while s != '':
    s_new = s[-3::] + ',' + s_new
    s = s[:-3]
print(s_new[:-1])
