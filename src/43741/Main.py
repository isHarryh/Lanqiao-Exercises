# 43741

text = input()

def compress(text: str):
    rst = ""
    char = ""
    count = 0
    for c in text:
        if c != char:
            rst += char
            if count > 1:
                rst += str(count)
            char = c
            count = 1
        else:
            count += 1
    rst += char
    if count > 1:
        rst += str(count)
    return rst

compressed = compress(text)

print(compressed if len(compressed) < len(text) else "NO")
