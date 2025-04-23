# 43727

n = int(input())

vertexes = [tuple(map(int, input().split())) for _ in range(n)]

import math

costs = [[0.0] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        p_i = vertexes[i]
        p_j = vertexes[j]
        c_ij = math.hypot(p_i[0] - p_j[0], p_i[1] - p_j[1]) + (p_i[2] - p_j[2]) ** 2
        costs[i][j] = c_ij
        costs[j][i] = c_ij

nearest = []

for i in range(n):
    row = list(range(n))
    row.remove(i)
    row.sort(key=lambda j: costs[i][j])
    nearest.append(row)

vertexes_included = set()
total_cost = 0.0

vertexes_included.add(0)
for i in range(n):
    if i != 0:
        nearest[i].remove(0)

while len(vertexes_included) != n:
    cost_min = -1
    cost_min_i = -1
    cost_min_j = -1
    for i in vertexes_included:
        j = nearest[i][0]
        if costs[i][j] < cost_min or cost_min < 0:
            cost_min = costs[i][j]
            cost_min_i = i
            cost_min_j = j

    # print(f"Connect {cost_min_i} + {cost_min_j}, cost {cost_min:.02f}")

    vertexes_included.add(cost_min_j)
    total_cost += cost_min

    for i in range(n):
        if i != cost_min_j:
            nearest[i].remove(cost_min_j)

print(f"{total_cost:.02f}")
