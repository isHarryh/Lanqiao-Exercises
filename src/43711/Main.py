# 43711

bottle = int(input())

cap = bottle
while cap >= 3:
    bottle += cap // 3
    cap = cap // 3 + cap % 3

print(bottle)
