n = int(input())
MOD = 10000

cache = [[0] * (n + 1) for _ in range(n + 1)]
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
prefix_sum_head = [0] * (n + 1)

def search(a, b):
    diff = abs(a - b)
    if diff <= 1:
        cache[a][b] = 1
        return 1

    head = min(diff - 1, prefix_sum_head[b])
    count = 1 + prefix_sum[b][head]
    count %= MOD

    for c in range(head + 1, diff):
        count += cache[b][c] if cache[b][c] > 0 else search(b, c)
        count %= MOD

    if b == prefix_sum_head[a] + 1:
        prefix_sum[a][b] = prefix_sum[a][b - 1] + count
        prefix_sum[a][b] %= MOD
        prefix_sum_head[a] = b

    cache[a][b] = count
    return count

total = 0
for m in range(1, n + 1):
    total += search(n, m)
    total %= MOD

print(total)
