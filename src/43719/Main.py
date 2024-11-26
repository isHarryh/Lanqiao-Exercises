# 43719

n = int(input())

def valid(x):
    while x != 0:
        if x % 10 == 2:
            return False
        x //= 10
    return True

print(sum(valid(i) for i in range(1, n + 1)))
