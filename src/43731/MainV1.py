# 43731

n, m, k = map(int, input().split())

packs = sorted(
    set(
        [tuple(set(map(int, input().split()))) for _ in range(n)]
    ),
    key=len,
    reverse=True
)

min_num_packs = -1

def dfs(i: int, selected: set, num_packs: int):
    global m, k, packs, min_num_packs
    if len(selected) == m:
        # Success
        if num_packs < min_num_packs or min_num_packs < 0:
            min_num_packs = num_packs
        return
    if i == len(packs):
        # Failure
        return

    pack = packs[i]
    dfs(i + 1, selected.union(pack), num_packs + 1)
    dfs(i + 1, selected, num_packs)

dfs(0, set(), 0)

print(min_num_packs)
