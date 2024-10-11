def chunked(symbols, n):
    new_list = []
    while symbols != []:
        new_list.append(symbols[:n])
        symbols = symbols[n:]
    return new_list


print(chunked(input().split(), int(input())))
