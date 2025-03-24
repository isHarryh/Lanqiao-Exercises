# 43722

n, m = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1

cur = 1
y, x = 0, 0
dx, dy = 1, 0
top, bottom, left, right = 0, n - 1, 0, m - 1

while y != r or x != c:
    if dy > 0 and y == bottom:
        dy = 0
        dx = -1
        right -= 1
    elif dy < 0 and y == top:
        dy = 0
        dx = 1
        left += 1
    elif dx > 0 and x == right:
        dy = 1
        dx = 0
        top += 1
    elif dx < 0 and x == left:
        dy = -1
        dx = 0
        bottom -= 1
    y += dy
    x += dx
    cur += 1
    # print(f"{cur}:\ty={y}\tx={x}")

print(cur)
