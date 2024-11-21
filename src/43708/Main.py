# 43708

txt = input().lower()
codes = [input().lower() for _ in range(int(input()))]

CODE_LEN = 8
LETTERS = "abcdefghijklmnopqrstuvwxyz"
LETTERS_LEN = len(LETTERS)

codes_stats = []
for c in codes:
    codes_stats.append(0)
    for l in range(LETTERS_LEN):
        codes_stats[-1] += c.count(LETTERS[l]) * (LETTERS_LEN ** l)

parts_stats = []
for i in range(len(txt) + 1 - 8):
    p = txt[i:i+8]
    parts_stats.append(0)
    for l in range(LETTERS_LEN):
        parts_stats[-1] += p.count(LETTERS[l]) * (LETTERS_LEN ** l)

count = 0
for cs in codes_stats:
    for ps in parts_stats:
        if ps == cs:
            count += 1

print(count)
