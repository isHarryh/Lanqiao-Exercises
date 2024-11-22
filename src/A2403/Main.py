# Fontaine

v, t, x = map(int, input().split())
MOD = 998244353

def pow(base, exp):
    global MOD
    rst = 1
    while exp > 0:
        if exp % 2 == 1:
            rst = (rst * base) % MOD
        base = (base * base) % MOD
        exp >>= 1
    return rst

print((v * pow(x, t)) % MOD)
