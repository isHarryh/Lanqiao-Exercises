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

def matrix_multiply(A, B):
    '''Multiplication for 6x6 matrices.'''
    result = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(6)) % MOD
    return result

def matrix_power(T, exp):
    '''Fast power for 6x6 matrices.'''
    result = [[1 if i == j else 0 for j in range(6)] for i in range(6)] # Identity matrix
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, T)
        T = matrix_multiply(T, T)
        exp //= 2
    return result

transit = [[True] * 6 for _ in range(6)]
'''`transit[a][b]` is `True` when up-face `a` can be transit to up-face `b`.'''
for a, b in conflict:
    transit[a][OPP[b]] = False
    transit[b][OPP[a]] = False

transitT = [[0] * 6 for _ in range(6)]
'''`transitT` is the transposed integer version of `transit`.'''
for i in range(6):
    for j in range(6):
        if transit[j][i]:
            transitT[i][j] = 1

transitTPowered = matrix_power(transitT, n - 1)
'''`transitT` power `n - 1`.'''

init = [1] * 6
final = [0] * 6

# Calculate `init` multiply by `transitTPowered`.
for i in range(6):
    final[i] = sum(transitTPowered[i][j] * init[j] for j in range(6)) % MOD

# Accumulate the result.
rst = sum(final) % MOD

# Multiply by `4^n` because the dice can be rotated by 90 degrees for 4 times.
rst = (rst * pow(4, n)) % MOD
print(rst)
