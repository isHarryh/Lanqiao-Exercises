# 43725

w = input()

aeiou = sum(w.count(l) for l in "aeiou")

print(aeiou)

print(len(w) - aeiou)
