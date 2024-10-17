# 43686

n = int(input())
x_nums = list(map(int, input().split()))
y_nums = list(map(int, input().split()))

DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))

def search(next_xy, cur_path, cur_x_nums, cur_y_nums):
    global n, x_nums, y_nums, DELTA

    cx, cy = next_xy
    cur_path.append(next_xy)
    cur_x_nums[cx] += 1
    cur_y_nums[cy] += 1

    # Judge whether exceeded the limit
    if cur_x_nums[cx] <= x_nums[cx] and cur_y_nums[cy] <= y_nums[cy]:
        # Judge whether reached the terminus
        if cx == n - 1 and cy == n - 1 and cur_x_nums == x_nums and cur_y_nums == y_nums:
            return cur_path
        # Walk to the next point
        for dx, dy in DELTA:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) not in cur_path and 0 <= nx < n and 0 <= ny < n:
                rst = search((nx, ny), cur_path, cur_x_nums, cur_y_nums)
                if rst:
                    return rst

    cur_x_nums[cx] -= 1
    cur_y_nums[cy] -= 1
    cur_path.pop()
    return None

def print_norm_path(path):
    global n
    for x, y in path:
        print(n * y + x, end=' ')

print_norm_path(search((0, 0), [], [0] * n, [0] * n))
