# 43717

n, m = map(int, input().split())
values = list(map(int, input().split()))

ranked = list(range(n))
ranked.sort(key=lambda i:values[i], reverse=True)

selected = []
for _ in range(m):
    for i in ranked:
        if (not selected or selected[-1] < i) and n - i >= m - len(selected):
            selected.append(i)
            ranked.remove(i)
            break

print(' '.join(map(lambda i:str(values[i]), selected)))
