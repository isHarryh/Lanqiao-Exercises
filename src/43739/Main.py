# 43739

text = input()

chars = set()

flag = True

for c in text:
    c = c.lower()
    if c in chars:
        flag = False
        break
    chars.add(c)

print("YES" if flag else "NO")
