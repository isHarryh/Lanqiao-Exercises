# 43695

init_situs = [list(input()) for _ in range(int(input()))]
cache = {}

def get_rate(cur_situ, atk_sign):
    global cache
    # Check the cached situations
    cur_situ_str = ''.join(cur_situ)
    id = f"{atk_sign}|{cur_situ_str}"
    if id in cache:
        return cache[id]

    # Calculate the winning rate of this situation
    next_rates = []
    for i in range(len(cur_situ)):
        if cur_situ[i] == '*':
            # For each empty position, fill in L or O
            for lo in 'LO':
                new_situ = cur_situ[:]
                new_situ[i] = lo
                new_situ_str = ''.join(new_situ)
                # Calculate the winning rate
                if 'LOL' in new_situ_str:
                    next_rates.append(1.0 if atk_sign else 0.0)
                elif '*' not in new_situ_str:
                    next_rates.append(0.5)
                else:
                    next_rates.append(get_rate(new_situ, not atk_sign))

    rst = max(next_rates) if atk_sign else min(next_rates)
    cache[id] = rst
    return rst

for situ in init_situs:
    rst = get_rate(situ, True)
    if rst == 1.0:
        print(1)
    elif rst == 0.0:
        print(-1)
    else:
        print(0)
