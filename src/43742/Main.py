# 43742

n, k = map(int, input().split())

block_1x1 = [[False] * n for _ in range(n)]
for y in range(n):
    for x, char in enumerate(list(input())):
        if char == "*":
            block_1x1[y][x] = True

def assign(mat: "list[list]", y: int, x: int):
    global n
    if 0 <= y < n and 0 <= x < n:
        mat[y][x] = True

def display(mat: "list[list]"):
    print()
    for row in mat:
        print(" ".join("#" if e else "-" for e in row))

block_3x3 = (
    [[True] * n] +
    [[True] + [False] * (n - 2) + [True] for _ in range(n - 2)] +
    [[True] * n]
)
for y in range(n):
    for x in range(n):
        if block_1x1[y][x]:
            assign(block_3x3, y - 1, x - 1)
            assign(block_3x3, y - 1, x)
            assign(block_3x3, y - 1, x + 1)
            assign(block_3x3, y, x - 1)
            assign(block_3x3, y, x)
            assign(block_3x3, y, x + 1)
            assign(block_3x3, y + 1, x - 1)
            assign(block_3x3, y + 1, x)
            assign(block_3x3, y + 1, x + 1)

block_5x5 = (
    [[True] * n] * 2 +
    [[True] * 2 + [False] * (n - 4) + [True] * 2 for _ in range(n - 4)] +
    [[True] * n] * 2
)
for y in range(n):
    for x in range(n):
        if block_3x3[y][x]:
            assign(block_5x5, y - 1, x - 1)
            assign(block_5x5, y - 1, x)
            assign(block_5x5, y - 1, x + 1)
            assign(block_5x5, y, x - 1)
            assign(block_5x5, y, x)
            assign(block_5x5, y, x + 1)
            assign(block_5x5, y + 1, x - 1)
            assign(block_5x5, y + 1, x)
            assign(block_5x5, y + 1, x + 1)

# display(block_1x1)
# display(block_3x3)
# display(block_5x5)

start = (2, 2)
final = (n - 3, n - 3)
DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs():
    global block_1x1, block_3x3, block_5x5, start, final, k
    fx, fy = final

    steps = 0
    queue = [start]
    visited = set([start])
    while queue:
        block = block_1x1 if steps > k + k else block_3x3 if steps > k else block_5x5
        steps += 1
        new_queue = []
        for x, y in queue:
            if block[y][x]:
                new_queue.append((x, y))
                continue
            if x == fx and y == fy:
                return steps - 1
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                nxy = (nx, ny)
                if 0 <= nx < n and 0 <= ny < n and nxy not in visited:
                    new_queue.append(nxy)
                    visited.add(nxy)
        queue = new_queue
    return False

print(bfs())
