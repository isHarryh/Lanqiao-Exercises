# 43718

n = int(input())
l = tuple(map(int, input().split()))

print(sum(all(i % j != 0 for j in l) for i in range(1, n + 1)))
