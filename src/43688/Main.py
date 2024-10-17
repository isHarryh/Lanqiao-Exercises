# 43688

n = int(input())

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
UNIT = len(CHARS)

left = n
rst = ""
while left > 0:
    left -= 1
    rst = CHARS[left % UNIT] + rst
    left //= UNIT

print(rst)
