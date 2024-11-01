s = input()
result = {}
min_word = 99999999999999
for word in s.split():
    word_stripped = word.strip('.,!?:;-').lower()
    result[word_stripped] = result.get(word_stripped, 0) + 1
for word in result:
    if result[word] < min_word:
        min_word = result[word]
result_word = 'яяя'
for key, value in result.items():
    if value == min_word and key < result_word:
        result_word = key
print(result_word)
