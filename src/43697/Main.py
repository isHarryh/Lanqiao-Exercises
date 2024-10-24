# 43697

import math

num_a, num_b = map(int, input().split())

# a + b = (n ** 2 + n) / 2
n = int((-1 + math.sqrt(1 + 8 * (num_a + num_b))) / 2)

count = 0
# For each possible situation of `n` floor
for n_val in range(1 << n):
    cur_a = 0
    cur_b = 0

    # Handle `n` floor
    cur_val = n_val
    # Sum up the occurrence of A(0) and B(1)
    for idx in range(n):
        if (cur_val >> idx) & 1:
            cur_b += 1
        else:
            cur_a += 1

    # Handle `n-1, n-2, ..., 2, 1` floor
    for cur in range(n - 1, 0, -1):
        # Calculate the value of the current floor
        cur_val = (((cur_val << 1) ^ cur_val) >> 1) & ~(1 << cur)
        # Sum up the occurrence of A(0) and B(1)
        for idx in range(cur):
            if (cur_val >> idx) & 1:
                cur_b += 1
            else:
                cur_a += 1
        # Break in advance if A or B exceeded the limit
        if cur_a > num_a or cur_b > num_b:
            break
        # print(f"{cur} => {bin(cur)[2:].zfill(n)}")

    # Increase the counter if this situation is valid
    if cur_a == num_a and cur_b == num_b:
        count += 1
    # print(f"a = {cur_a}, b = {cur_b}")

print(count)
