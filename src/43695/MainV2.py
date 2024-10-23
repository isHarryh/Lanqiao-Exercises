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
    rate = None
    for i in range(len(cur_situ_str)):
        if cur_situ_str[i] == '*':
            # For each empty position, fill in L or O
            for lo in 'LO':
                new_situ = cur_situ[:]
                new_situ[i] = lo
                new_situ_str = ''.join(new_situ)
                # Calculate the winning rate of each action
                if 'LOL' in new_situ_str:
                    new_rate = atk_sign
                elif '*' not in new_situ_str:
                    new_rate = 0
                else:
                    new_rate = get_rate(new_situ, -1 * atk_sign)
                if new_rate == atk_sign:
                    # Reached the limit, best action found in advance
                    cache[id] = new_rate
                    return new_rate
                if rate is None or new_rate * atk_sign > rate * atk_sign:
                    # Renew the pending winning rate of this situation
                    rate = new_rate

    # Cache this situation and return
    cache[id] = rate
    return rate

for situ in init_situs:
    print(get_rate(situ, 1))
