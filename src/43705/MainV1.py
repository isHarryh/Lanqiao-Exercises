# 43705

n, m = map(int, input().split())

# Note that point 1~6 are mapped to 0~5
conflict = [tuple(map(lambda x:int(x) - 1, input().split())) for _ in range(m)]

OPP = [3, 4, 5, 0, 1, 2]
'''`OPP[a]` is `b` means the opposite side of face `a` is face `b`.'''

MOD = 1000000007

def pow(base, exp):
    '''Fast power for integer.'''
    global MOD
    rst = 1
    while exp > 0:
        if exp % 2 == 1:
            rst = (rst * base) % MOD
        base = (base * base) % MOD
        exp >>= 1
    return rst

transit = [[True] * 6 for _ in range(6)]
'''`transit[a][b]` is `True` when up-face `a` can be transit to up-face `b`.'''
for a, b in conflict:
    transit[a][OPP[b]] = False
    transit[b][OPP[a]] = False

dp = [1] * 6
'''`dp[i]` represents the number of ways to form up-face `i` on top.'''
for _ in range(1, n):
    dp = [sum([dp[last] * transit[last][this] for last in range(6)]) % MOD for this in range(6)]

# Multiply by `4^n` because the dice can be rotated by 90 degrees for 4 times.
print((sum(dp) * pow(4, n)) % MOD)
