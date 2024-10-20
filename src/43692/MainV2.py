# 43692

origin = input()
target = input()

CHARS = "*WB"
BASE = len(CHARS)
LENGTH = len(origin)
DELTA = (-3, -2, -1, 1, 2, 3)
POW_TABLE = [pow(BASE, e) for e in range(LENGTH)]

def map_to_int(s):
    """Converts the situation string to equivalent integer."""
    global CHARS, BASE
    rst = 0
    for idx, char in enumerate(s):
        rst += CHARS.index(char) * pow(BASE, idx)
    return rst

origin = map_to_int(origin)
target = map_to_int(target)

def search(cur_situs, searched_situs, cur_steps):
    global target, BASE, LENGTH
    next_situs = set()

    for cur in cur_situs:
        searched_situs.add(cur)
        # Find the position with value 0
        for i in range(LENGTH):
            if cur // POW_TABLE[i] % BASE == 0:
                empty_i = i
                # Try different positions to swap
                for d in DELTA:
                    frog_i = empty_i + d
                    if 0 <= frog_i < LENGTH:
                        # Retrieve the frog value
                        frog_val = cur // POW_TABLE[frog_i] % BASE
                        # Do swap
                        next = cur
                        next += frog_val * POW_TABLE[empty_i]
                        next -= frog_val * POW_TABLE[frog_i]
                        # Judge success or not
                        if next == target:
                            return cur_steps
                        if next not in searched_situs:
                            next_situs.add(next)
                break

    # Goto the next searching iteration
    return search(next_situs, searched_situs, cur_steps + 1)

print(search(set([origin]), set(), 1))
