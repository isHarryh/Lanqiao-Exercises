# 43720

word = input()

LETTERS = "abcdefghijklmnopqrstuvwxyz"
TABLE = {LETTERS[i]: LETTERS[i + 3 if i < 23 else i - 23] for i in range(len(LETTERS))}

new_word = ""
for c in word:
    new_word += TABLE[c]

print(new_word)
