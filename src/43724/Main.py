# 43724

m, n = map(int, input().split())
MOD = 10000

if m < 2 or n < 2:
    print(0)
else:
    # cur_m=1 (next=2)
    cur_count = [0] * (n + 2)
    next_count = [0] * (n + 2)

    next_sum = 0
    for x in range(1, n + 1):
        next_count[x] = (n - x) % MOD
        next_sum += next_count[x]
    # print(f"m={1}\tnext={next_count[1:-1]}\t(next_sum={next_sum})")

    # cur_m=2 (next=3), cur_m=3 (next=4), ..., cur_m=m-1 (next=m)
    for cur_m in range(2, m):
        swap = cur_count
        cur_count = next_count
        next_count = swap

        cur_sum = next_sum
        next_sum = 0
        for x in (range(n, 0, -1) if cur_m % 2 == 0 else range(1, n + 1)):
            cur_sum -= cur_count[x]
            next_count[x] = cur_sum % MOD
            next_sum += next_count[x]
        # print(f"m={cur_m}\tcur={cur_count[1:-1]}\tnext={next_count[1:-1]}\t(next_sum={next_sum})")

    print(next_sum % MOD)
