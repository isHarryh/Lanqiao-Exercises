# 43731

n, m, k = map(int, input().split())

import functools

packs = list(
    set(
        functools.reduce(
            int.__or__,
            (1 << (x - 1) for x in map(int, input().split())),
            0
        ) for _ in range(n)
    )
)

INF = n + 1

dp = [INF] * (1 << m)
dp[0] = 0

for pack in packs:
    for raw in range(1 << m):
        if dp[raw] < INF:
            added = raw | pack
            dp[added] = min(dp[added], dp[raw] + 1)

print(dp[(1 << m) - 1] if dp[(1 << m) - 1] < INF else -1)
