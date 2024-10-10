n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
n2 = int(input())
result = 'НЕТ'
for i in range(n - 1):
    for j in range(i + 1, n):
        if numbers[i] * numbers[j] == n2:
            result = 'ДА'
print(result)
