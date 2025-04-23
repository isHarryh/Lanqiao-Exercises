# 43729

n = int(input())

nodes = iter(map(int, input().split()))

max_r = 0
max_s = 0

r = 1
while True:
    try:
        s = 0
        for i in range(1 << (r - 1), 1 << r):
            # i = 2^(r-1), ..., 2^r - 1
            s += next(nodes)
    except StopIteration:
        break
    finally:
        if s > max_s:
            max_r = r
            max_s = s
        r += 1

print(max_r)
