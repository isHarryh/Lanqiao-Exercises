# 43692

origin = input()
target = input()
length = len(origin)

DELTA = (-3, -2, -1, 1, 2, 3)

def search(cur_situs, cur_steps):
    global target, length
    next_situs = set()

    for cur in cur_situs:
        # Find the position with char *
        empty_i = cur.index('*')
        # Try different positions to swap
        for d in DELTA:
            if 0 <= empty_i + d < length:
                min_i = min(empty_i, empty_i + d)
                max_i = max(empty_i, empty_i + d)
                next = cur[:min_i] + cur[max_i] + cur[min_i + 1:max_i] + cur[min_i] + cur[max_i + 1:]
                # Judge success or not
                if next == target:
                    return cur_steps
                next_situs.add(next)

    # Goto the next searching iteration
    return search(next_situs, cur_steps + 1)

print(search(set([origin]), 1))
