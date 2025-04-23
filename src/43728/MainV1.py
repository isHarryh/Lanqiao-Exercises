# 43728

n = int(input())

trees = [tuple(map(int, input().split())) for _ in range(n)]

values = [r * r for _, _, r in trees]

collided = [[False] * n for _ in range(n)]

import math

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x1, y1, r1 = trees[i]
        x2, y2, r2 = trees[j]
        if math.hypot(x1 - x2, y1 - y2) < r1 + r2:
            collided[i][j] = True
            collided[j][i] = True

max_value = 0
max_value_selected = []

mask = (1 << n) - 1

while mask > 0:
    valid = True
    selected = []
    for i in range(n):
        if (mask >> i) & 1:
            if any(collided[i][j] for j in selected):
                valid = False
                break
            selected.append(i)
    if valid:
        cur_value = sum(values[i] for i in selected)
        if max_value < cur_value or not max_value:
            max_value = cur_value
            max_value_selected = selected
    mask -= 1

print(max_value)
# print(max_value_selected)
