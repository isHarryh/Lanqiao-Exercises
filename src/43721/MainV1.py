# 43721

n = int(input())
values = list(map(int, input().split()))

cur_max = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        cur = j - i + abs(values[i] - values[j])
        cur_max = cur if cur > cur_max else cur_max

print(cur_max)
