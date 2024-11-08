symbols = {}
code = input()
for symbol in code:
    symbols[symbol] = symbols.get(symbol, 0) + 1
letters = {}
for _ in range(int(input())):
    letter, count = input().split(': ')
    letters[int(count)] = letter
for i in code:
    print(letters[symbols[i]], end='')
