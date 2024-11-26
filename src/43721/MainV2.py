# 43721

n = int(input())
values = list(map(int, input().split()))

s1 = [x + values[x] for x in range(n)]
s2 = [x - values[x] for x in range(n)]
s3 = [- x + values[x] for x in range(n)]
s4 = [- x - values[x] for x in range(n)]

print(max(max(s1) - min(s1), max(s2) - min(s2), max(s3) - min(s3), max(s4) - min(s4)))
