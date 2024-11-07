# 43703

n = int(input())

cache = {}

def get_max(init):
    global cache
    cur_n = init
    cur_max = init
    while cur_n > 1:
        if cur_n in cache:
            if cache[cur_n] >= cur_max:
                cur_max = cache[cur_n]
            break
        if cur_n % 2 == 0:
            cur_n = cur_n // 2
        else:
            cur_n = cur_n * 3 + 1
            if cur_n > cur_max:
                cur_max = cur_n
    cache[init] = cur_max
    return cur_max

global_max = 0
global_max_i = 0
for i in range(1, n + 1):
    this_max = get_max(i)
    if this_max > global_max:
        global_max = this_max
        global_max_i = i

print(global_max)
