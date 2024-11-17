# 43706

m, n = map(int, input().split())

w = n + m - 1

for y in range(n):
    head = y
    tail = n - y - 1
    line = ""
    for x in range(w):
        line += '*' if head <= x < head + m or tail <= x < tail + m else '.'
    print(line)
