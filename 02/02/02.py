total = 0
numbers = list(map(int, input().split()))
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        total += 1
print(total)
