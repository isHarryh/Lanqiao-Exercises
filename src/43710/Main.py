# 43710

n = int(input())
SRC = 'A'
DST = 'B'
POS = '+'
NEG = '-'

mat = [input().split() for _ in range(n)]
DELTA = ((1, 0), (0, 1), (-1, 0), (0, -1))

# Find the initial point
init = None
for y in range(n):
    for x in range(n):
        if mat[y][x] == SRC:
            init = (x, y)

best_depth = -1

# For each initial sign
for sign in (POS, NEG):
    depth = 0
    found = False
    queue = [init]
    searched = [[False for _ in range(n)] for _ in range(n)]
    # Do BFS
    while not found:
        depth += 1
        new_queue = []
        # For each point searched in the last depth
        for x, y in queue:
            searched[y][x] = True
            for dx, dy in DELTA:
                nx = x + dx
                ny = y + dy
                # Ensure the new point has not been searched
                if 0 <= nx < n and 0 <= ny < n and not searched[ny][nx]:
                    if mat[ny][nx] == sign:
                        new_queue.append((nx, ny))
                    elif mat[ny][nx] == DST:
                        found = True
        # Stop searching if no new point is available
        if not new_queue:
            break
        # Revert the sign for the next depth searching
        queue = new_queue
        sign = POS if sign == NEG else NEG
    # Update the best result
    if found:
        best_depth = depth if best_depth < 0 else min(best_depth, depth)

print(best_depth)
