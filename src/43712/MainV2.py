# 43712

import math

n = int(input())

cache = {x: [x] if 1 <= x <= n else [] for x in range(10)}
total = sum(len(l) for l in cache.values())

for _ in range(math.floor(math.log10(n))):
    new_cache = {x: [] for x in range(10)}
    for tail in range(10):
        for new_tail in range(tail, 10):
            for val in cache[tail]:
                new_val = val * 10 + new_tail
                if new_val <= n:
                    new_cache[new_tail].append(new_val)
    total += sum(len(l) for l in new_cache.values())
    cache = new_cache

print(total)
