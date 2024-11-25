# 43715

n, m = map(int, input().split())
mat = [[True if i == 'g' else False for i in input()] for _ in range(n)]
k = int(input())

DELTA = ((1, 0), (-1, 0), (0, 1), (0, -1))

def find_grow_points(mat):
    global n, m
    rst = set()
    for y in range(n):
        for x in range(m):
            if mat[y][x]:
                rst.add((x, y))
    return rst

def grow_grow_grow(mat, grow_points, epochs):
    global n, m, DELTA
    rst = mat[:]
    for _ in range(epochs):
        new_grow_points = set()
        for gx, gy in grow_points:
            for dx, dy in DELTA:
                nx = gx + dx
                ny = gy + dy
                if 0 <= nx < m and 0 <= ny < n and not rst[ny][nx]:
                    rst[ny][nx] = True
                    new_grow_points.add((nx, ny))
        if not len(new_grow_points):
            break
        grow_points = new_grow_points
    return rst

rst = grow_grow_grow(mat, find_grow_points(mat), k)
for y in range(n):
    l = ""
    for x in range(m):
        l += 'g' if rst[y][x] else '.'
    print(l)
