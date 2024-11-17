# 43707

this = input()
n = int(input())

for _ in range(n):
    next = ""
    char = ''
    count = 0
    for i in this:
        if i == char:
            count += 1
        else:
            if count:
                next += str(count) + char
            char = i
            count = 1
    if count:
        next += str(count) + char
    this = next

print(this)
