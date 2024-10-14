n, m = int(input()), int(input())
x_max = y_max = 0
max_element = -100000000
for i in range(n):
    new_string = input().split()
    for j in range(m):
        if int(new_string[j]) > max_element:
            max_element = int(new_string[j])
            x_max = i
            y_max = j
print(x_max, y_max)
