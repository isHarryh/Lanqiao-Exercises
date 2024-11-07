# 43704

w, m, n = map(int, input().split())

def is_reversed(num):
    global w
    return (num - 1) % (w << 1) // w

def get_y(num):
    global w
    return (num - 1) // w

def get_x(num):
    global w
    if is_reversed(num):
        return w * (get_y(num) + 1) - num
    else:
        return num - 1 - w * get_y(num)

print(abs(get_y(m) - get_y(n)) + abs(get_x(m) - get_x(n)))
