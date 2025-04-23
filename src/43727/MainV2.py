# 43727

n = int(input())

vertexes = [tuple(map(int, input().split())) for _ in range(n)]

import math
import heapq

min_heap = []
min_heap.append((0.0, 0))  # (cost, vertex_index)
heapq.heapify(min_heap)

vertexes_visited = [False] * n

total_cost = 0.0

while min_heap:
    c, i = heapq.heappop(min_heap)
    if vertexes_visited[i]:
        continue
    vertexes_visited[i] = True
    total_cost += c

    # print(f"Connect {i}, cost {c:.02f}")

    for j in range(n):
        if not vertexes_visited[j]:
            p_i = vertexes[i]
            p_j = vertexes[j]
            c_ij = math.hypot(p_i[0] - p_j[0], p_i[1] - p_j[1]) + (p_i[2] - p_j[2]) ** 2
            heapq.heappush(min_heap, (c_ij, j))

print(f"{total_cost:.02f}")
