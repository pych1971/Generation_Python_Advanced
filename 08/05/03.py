sentence = input().split()
sentence_set = set()
for i in sentence:
    sentence_set.add(i.lower().strip('.,;:-?!'))
print(len(sentence_set))
