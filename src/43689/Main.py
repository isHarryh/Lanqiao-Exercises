# 43689

import math
from functools import reduce

n = int(input())
nums = [int(input()) for _ in range(n)]

gcd = reduce(math.gcd, nums)
if gcd != 1:
    print("INF")
else:
    dp = set([0])
    end = 1 << 16
    count = 0
    for i in range(1, end):
        for n in nums:
            if i - n in dp:
                dp.add(i)
                break
    print(end - len(dp))
