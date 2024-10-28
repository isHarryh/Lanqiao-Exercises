# 43700

n_list = list(map(int, input().split()))
init_list = list(map(int, input().split()))

cache = {}

def get_rate(cur, atk_has, def_has, atk_sign):
    global n_list
    # Check the cached situations
    id = f"{cur}|{atk_has % 2}|{def_has % 2}|{atk_sign}"
    if id in cache:
        return cache[id]

    rate = None
    for n in n_list:
        left = cur - n
        if left >= 0:
            # Can fetch ball
            if atk_sign:
                new_rate = get_rate(left, atk_has + n, def_has, False)
                # Atk should maximize the winning rate
                if rate is None or new_rate > rate:
                    rate = new_rate
            else:
                new_rate = get_rate(left, atk_has, def_has + n, True)
                # Def should minimize the winning rate
                if rate is None or new_rate < rate:
                    rate = new_rate

    if rate is None:
        # Cannot fetch more ball then check who wins
        # 1=atk_win, 0=nobody_win, -1=def_win
        rate = atk_has % 2 - def_has % 2

    cache[id] = rate
    return rate

for init in init_list:
    rst = get_rate(init, 0, 0, True)
    print({1: '+', 0: '0', -1: '-'}[rst], end=' ')
