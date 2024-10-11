text = input().split()
new_list = [list(text[0])]
for i in range(1, len(text)):
    if text[i] == new_list[-1][-1]:
        new_list[-1].append(text[i])
    else:
        new_list.append(list(text[i]))
print(new_list)
