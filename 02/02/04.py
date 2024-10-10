numbers = input().split()
numbers.insert(0, numbers[-1])
numbers.pop(-1)
print(*numbers)
