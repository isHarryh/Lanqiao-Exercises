# 43693

origin = list(map(int, input().split('/')))

NORMAL_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
RUN_MONTHS = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
ORDERS = ((0, 1, 2), (2, 0, 1), (2, 1, 0))

def convert(y, m, d):
    if m <= 0 or m > 12:
        return None
    y = 2000 + y if y < 60 else 1900 + y
    is_run = y % 400 == 0 or y % 4 == 0 and y % 100 != 0
    if d <= 0 or d > (RUN_MONTHS[m - 1] if is_run else NORMAL_MONTHS[m - 1]):
        return None
    return f"{y:04}-{m:02}-{d:02}"

rst = [convert(*tuple(origin[i] for i in o)) for o in ORDERS]
for i in sorted(set(filter(lambda x:x, rst))):
    print(i)
