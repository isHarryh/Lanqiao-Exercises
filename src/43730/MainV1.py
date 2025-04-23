# 43730

n = int(input())

arr = list(map(int, input().split()))

top = 1

exists = set()

for i, val in enumerate(arr):
    if val < top:
        val = top
        top += 1
    else:
        while val in exists:
            val += 1
    arr[i] = val
    exists.add(val)
    while top in exists:
        top += 1

print(" ".join(map(str, arr)))
