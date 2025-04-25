# 43737

n = int(input())

if n > 100:
    print("0.61803399")
else:
    a = 0
    b = 0
    c = 1

    i = 1
    while i < n + 1:
        a = b
        b = c
        c = a + b
        i += 1

    print(f"{b / c:.8f}")
