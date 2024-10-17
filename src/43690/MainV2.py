# 43690

origin_mat = [list(map(int, input().split())) for _ in range(3)]
# origin_mat = [[0, 7, 2], [0, 5, 0], [0, 3, 0]]
# origin_mat = [[0, 0, 0], [0, 5, 0], [0, 0, 0]]

def find_missing_nums(mat):
    nums = list(range(10))
    for row in mat:
        for n in row:
            if n in nums:
                nums.remove(n)
    return nums

def verify(mat):
    return mat[0][0] + mat[1][0] + mat[2][0] == mat[0][1] + mat[1][1] + mat[2][1] == \
    mat[0][2] + mat[1][2] + mat[2][2] == mat[0][0] + mat[0][1] + mat[0][2] == \
    mat[1][0] + mat[1][1] + mat[1][2] == mat[2][0] + mat[2][1] + mat[2][2] == \
    mat[0][0] + mat[1][1] + mat[2][2] == mat[2][0] + mat[1][1] + mat[0][2]

def has_hope(mat):
    if mat[1][1] not in (0, 5):
        return False
    for idx in range(3):
        if mat[idx][0] and mat[idx][1] and mat[idx][2]:
            if sum(mat[idx]) != 15:
                return False
        if mat[0][idx] and mat[1][idx] and mat[2][idx]:
            if mat[0][idx] + mat[1][idx] + mat[2][idx] != 15:
                return False
    if mat[0][0] and mat[1][1] and mat[2][2]:
        if mat[0][0] + mat[1][1] + mat[2][2] != 15:
            return False
    if mat[0][2] and mat[1][1] and mat[2][0]:
        if mat[0][2] + mat[1][1] + mat[2][0] != 15:
            return False
    return True

def search(all_rst, cur_mat, missing_nums):
    if not missing_nums:
        if verify(cur_mat):
            all_rst.add(','.join(str(n) for row in cur_mat for n in row))
            if len(all_rst) > 1:
                print("Too Many")
                exit(0)
    else:
        for y in range(len(cur_mat)):
            for x in range(len(cur_mat[y])):
                if cur_mat[y][x] == 0:
                    for i in range(len(missing_nums)):
                        n = missing_nums[i]
                        cur_mat[y][x] = n
                        if has_hope(cur_mat):
                            missing_nums.pop(i)
                            search(all_rst, cur_mat, missing_nums)
                            missing_nums.insert(i, n)
                        cur_mat[y][x] = 0
    return all_rst

rst = search(set(), origin_mat, find_missing_nums(origin_mat))

for mat_str in rst:
    mat_str = mat_str.split(',')
    for idx, n in enumerate(mat_str):
        print(n, end='\n' if (idx + 1) % 3 == 0 else ' ')
