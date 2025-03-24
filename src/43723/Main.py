# 43723

n = int(input())
arr = tuple(map(int, input().split()))

m = 0
best_m = 0
prev = arr[0]

for cur in arr:
    if cur > prev:
        m = m + 1 if m > 0 else 2
    else:
        best_m = max(m, best_m)
        m = 0
    prev = cur

print(best_m)
