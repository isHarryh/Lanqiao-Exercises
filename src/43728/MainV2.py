# 43728

n = int(input())

trees = [tuple(map(int, input().split())) for _ in range(n)]

values = [r * r for _, _, r in trees]

order = sorted(range(n), key=lambda i: -values[i])

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
max_value_selected = set()

def dfs(k: int, selected: set, current_value: int):
    global max_value, max_value_selected

    if k == n:
        # Finished
        if current_value > max_value:
            max_value = current_value
            max_value_selected = selected.copy()
        return

    remaining_upper_bound = current_value + sum(values[order[j]] for j in range(k, n))
    if remaining_upper_bound <= max_value:
        return

    i = order[k]

    # Select tree i (if not collided with existing trees)
    if all(not collided[i][j] for j in selected):
        selected.add(i)
        dfs(k + 1, selected, current_value + values[i])
        selected.remove(i)

    # Not select tree i
    dfs(k + 1, selected, current_value)

dfs(0, set(), 0)

print(max_value)
# print(max_value_selected)
