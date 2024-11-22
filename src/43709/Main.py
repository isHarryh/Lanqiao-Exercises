# 43709

n, s = map(int, input().split())
MAX = 10 ** 51

def eval(init, n):
    new = init
    rst = init
    for _ in range(n):
        new <<= 1
        new -= 1
        rst += new
    return rst

def find(init_min, init_max, n, s):
    if init_min > init_max:
        return -1
    init = init_min + (init_max - init_min) // 2
    test = eval(init, n)
    if test == s:
        return init
    elif test > s:
        return find(init_min, init - 1, n, s)
    else:
        return find(init + 1, init_max, n, s)

print(find(0, MAX, n, s))
