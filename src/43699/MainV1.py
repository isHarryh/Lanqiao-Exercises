# 43699

import math
import sys

n = int(input())

m = int(math.sqrt(n)) + 1

for a in range(0, m):
    for b in range(a, m):
        for c in range(b, m):
            for d in range(c, m):
                if a * a + b * b + c * c + d * d == n:
                    print(a, b, c, d)
                    sys.exit(0)
