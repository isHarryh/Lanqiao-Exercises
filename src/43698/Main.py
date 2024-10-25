# 43698

import math

n = int(input())
amounts = list(map(int, input().split()))
sorted_amounts = sorted(set(amounts))

best_scale = None
guess_a = None
guess_b = None

for i in range(len(sorted_amounts) - 1):
    a = sorted_amounts[i + 1]
    b = sorted_amounts[i]
    if best_scale is None or a / b < guess_a / guess_b:
        best_scale = a / b
        guess_a = a
        guess_b = b

gcd = math.gcd(guess_a, guess_b)
print(f"{guess_a // gcd}/{guess_b // gcd}")
