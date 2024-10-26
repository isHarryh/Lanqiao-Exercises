# 43699

import math
import sys

n = int(input())

m = int(math.sqrt(n)) + 1

CCDD_TABLE = {}
for c in range(0, m):
    for d in range(c, m):
        ccdd = c * c + d * d
        if ccdd not in CCDD_TABLE:
            CCDD_TABLE[ccdd] = (c, d)

for a in range(0, m):
    for b in range(a, m):
        remain = n - a * a - b * b
        if remain in CCDD_TABLE:
            c, d = CCDD_TABLE[remain]
            print(a, b, c, d)
            sys.exit(0)
