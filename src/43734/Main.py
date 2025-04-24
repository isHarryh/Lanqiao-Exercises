# 43734

h, w = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(h)]

def print_rotated(mat: "list[list[int]]", h: int, w: int):
    new_mat = []
    for x in range(w):
        new_row = []
        for y in range(h - 1, -1, -1):
            new_row.append(mat[y][x])
        new_mat.append(new_row)
        print(" ".join(map(str, new_row)))
    return new_mat

print_rotated(mat, h, w)
