# 43730

n = int(input())

arr = list(map(int, input().split()))

parent = {}

def find(x):
    if x not in parent:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for i, val in enumerate(arr):
    new_val = find(val)
    arr[i] = new_val
    parent[new_val] = find(new_val + 1)

print(" ".join(map(str, arr)))
