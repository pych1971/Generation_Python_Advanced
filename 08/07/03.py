grades1 = set(map(int, input().split()))
grades2 = set(map(int, input().split()))
grades3 = set(map(int, input().split()))
print(*sorted(grades1 & grades2 - grades3, reverse=True))
