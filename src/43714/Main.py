# 43714

word = input().lower()
VOWELS = "aeiou"

def match(word, pattern):
    global VOWELS
    i = 0
    n = len(word)
    for p in pattern:
        flag = False
        while i < n and (p == 'V') ^ (word[i] not in VOWELS):
            i += 1
            flag = True
        if not flag:
            return False
    return i >= n

print('yes' if match(word, "CVCV") else 'no')
