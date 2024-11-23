# 43712

n = int(input())

def is_valid(x):
    t = 10
    while x != 0:
        c = x % 10
        if c > t:
            return False
        t = c
        x //= 10
    return True

print(sum(is_valid(i) for i in range(1, n + 1)))
