# 43708

txt = input()
codes = [input() for _ in range(int(input()))]

CODE_LEN = 8
LETTERS = "abcdefghijklmnopqrstuvwxyz"
LETTERS_LEN = len(LETTERS)
POW_TABLE = [pow(CODE_LEN, i) for i in range(LETTERS_LEN)]

codes_stats = []
for c in codes:
    codes_stats.append(0)
    for l in range(LETTERS_LEN):
        codes_stats[-1] += c.count(LETTERS[l]) * POW_TABLE[l]

parts_stats = []
for i in range(len(txt) + 1 - CODE_LEN):
    p = txt[i:i + CODE_LEN]
    parts_stats.append(0)
    for l in range(LETTERS_LEN):
        parts_stats[-1] += p.count(LETTERS[l]) * POW_TABLE[l]

count = 0
for cs in codes_stats:
    for ps in parts_stats:
        if ps == cs:
            count += 1

print(count)
