dictionary = {}
for _ in range(int(input())):
    word, syn = input().split()
    dictionary[word] = syn
    dictionary[syn] = word
print(dictionary[input()])
