word1 = {}
for i in input():
    word1[i] = word1.get(i, 0) + 1
word2 = {}
for i in input():
    word2[i] = word2.get(i, 0) + 1
if word1 == word2:
    print('YES')
else:
    print('NO')
