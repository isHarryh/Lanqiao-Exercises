# 43687

n = int(input())
origin_li = list(map(int, input().split()))

def test_on(start_idx):
    global n, origin_li
    li = origin_li[:]

    tot = 0
    cur = 1
    idx = start_idx
    while True:
        if cur == li[idx]:
            tot += cur
            cur = 1
            li.pop(idx)
        else:
            cur += 1
            idx += 1
        if idx == len(li):
            idx = 0
        if cur > n or not li:
            return tot

max_i = -1
max_t = -1
for i in range(n):
    t = test_on(i)
    if max_t < t:
        max_i = i
        max_t = t

print(max_t)
