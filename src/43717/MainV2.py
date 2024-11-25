# 43717

n, m = map(int, input().split())
values = list(map(int, input().split()))

selected = []
for i in range(n):
    while selected and n - i > m - len(selected) and values[selected[-1]] < values[i]:
        selected.pop()
    if len(selected) < m:
        selected.append(i)
    else:
        break

print(' '.join(map(lambda i:str(values[i]), selected)))
