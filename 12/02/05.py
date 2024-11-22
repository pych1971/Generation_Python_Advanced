from random import shuffle

word = input()
word_list = list(word)
shuffle(word_list)
print(*word_list, sep='')
