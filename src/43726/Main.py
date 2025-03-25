# 43726

n, m = map(int, input().split())
n -= 1
m -= 1

d = float(input())
robust_d = d + 1e-6

import math

nm_d = math.hypot(n, m)
cnt = 1

while nm_d > d:
    x = d * m / nm_d
    y = d * n / nm_d
    ceil_x = math.ceil(x)
    ceil_y = math.ceil(y)
    floor_x = math.floor(x)
    floor_y = math.floor(y)

    """
        |     |
    --- A --- B ---
        |     |
    --- D --- C ---
        |     |
    """

    can_ceil_xy = math.hypot(ceil_x, ceil_y) < robust_d

    if can_ceil_xy:
        # Choose point B
        jmp_x = ceil_x
        jmp_y = ceil_y
    else:
        can_ceil_x = math.hypot(ceil_x, floor_y) < robust_d
        can_ceil_y = math.hypot(floor_x, ceil_y) < robust_d

        if can_ceil_y and not (can_ceil_x and n < m):
            # Choose point A
            jmp_x = floor_x
            jmp_y = ceil_y
        elif can_ceil_x:
            # Choose point C
            jmp_x = ceil_x
            jmp_y = floor_y
        else:
            # Choose point D
            jmp_x = floor_x
            jmp_y = floor_y

    n -= jmp_y
    m -= jmp_x
    jmp_d = math.hypot(jmp_x, jmp_y)
    nm_d = math.hypot(n, m)
    # print(f"#{cnt}: jump=({jmp_x}, {jmp_y}):{jmp_d:.2f}\tremaining=({m}, {n}):{nm_d:.2f}")
    cnt += 1

print(cnt)
