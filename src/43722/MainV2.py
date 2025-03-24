# 43722

n, m = map(int, input().split())
r, c = map(int, input().split())

r -= 1
c -= 1

k = min(r, c, n - r - 1, m - c - 1)

pre_sum = 0
for i in range(k):
    h = n - 2 * i
    w = m - 2 * i
    pre_sum += 2 * (w + h) - 4

cur_h = n - 2 * k
cur_w = m - 2 * k

rst = pre_sum
if r == k:
    # Top
    rst += 1 + c - k
elif c == m - k - 1:
    # Right
    rst += cur_w + (r - k)
elif r == n - k - 1:
    # Bottom
    rst += (cur_w + cur_h - 1) + (m - k - c - 1)
elif c == k:
    # Left
    rst += (cur_w + cur_h + cur_w - 2) + (n - k - r - 1)

print(rst)
