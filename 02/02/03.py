numbers = list(map(int, input().split()))
for i in range(1, len(numbers), 2):
    numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
print(*numbers)
