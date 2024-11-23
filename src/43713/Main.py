# 43713

n = int(input())
li = list(map(int, input().split()))

min_li = [-1] * n
for i in range(n):
    min_li[i] = li[i] if i == 0 or li[i] < min_li[i - 1] else min_li[i - 1]

max_li = [-1] * n
for i in range(n - 1, -1, -1):
    max_li[i] = li[i] if i == n - 1 or li[i] > max_li[i + 1] else max_li[i + 1]

total = 0
for i in range(1, n - 1):
    if min_li[i - 1] < li[i] < max_li[i + 1]:
        total += 1
print(total)
