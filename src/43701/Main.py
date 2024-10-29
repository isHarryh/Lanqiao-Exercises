# 43701

s = input()
n = len(s)
dp = [[0] * n for _ in range(n)]

# For sub string length from `2` to `n`
for sub_len in range(2, n + 1):
    '''
    For each sub string length, iterate i and j like this:
    |i===j-------|
    |-i===j------|
    |--i===j-----|
    ...
    |-------i===j|
    '''
    # Left index (i) from `0` to `n - sub_len`
    for i in range(n - sub_len + 1):
        # Right index (j) from `sub_len - 1` to `n - 1`
        j = i + sub_len - 1
        if s[i] == s[j]:
            # Current result is previous result
            dp[i][j] = dp[i + 1][j - 1]
        else:
            # Current result is previous minimal result + 1
            dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

print(dp[0][n - 1])
