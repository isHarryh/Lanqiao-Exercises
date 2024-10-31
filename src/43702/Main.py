# 43702

n = int(input())
init = list(map(int, input().split()))
swaps = [(init.index(x) + 1) for x in range(1, n + 1)]

count = 0
searched = []
for idx in range(n):
    val = init[idx]
    if val not in searched:
        swap = None
        cur_values = []
        while swap not in cur_values:
            searched.append(val)
            cur_values.append(val)
            swap = swaps[val - 1]
            val = swap
        count += len(cur_values) - 1

print(count)
