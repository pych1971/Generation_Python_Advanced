grades1 = set(map(int, input().split()))
grades2 = set(map(int, input().split()))
grades3 = set(map(int, input().split()))
print(*sorted(grades3 - (grades1 | grades2), reverse=True))
