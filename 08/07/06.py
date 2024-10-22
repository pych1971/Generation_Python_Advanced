grades1 = set(map(int, input().split()))
grades2 = set(map(int, input().split()))
grades3 = set(map(int, input().split()))
print(*sorted({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - (grades1 | grades2 | grades3)))
