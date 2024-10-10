numbers = input().split()
difference = 1
for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        difference += 1
print(difference)
