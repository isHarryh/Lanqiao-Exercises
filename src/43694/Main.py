# 43694

reg = input()

def get_max_length(reg):
    values = [0]
    brackets = []
    for i, c in enumerate(reg):
        if c == '(':
            brackets.append(i)
        elif c == ')':
            left = brackets.pop()
            if not brackets:
                right = i
                values[-1] += get_max_length(reg[left + 1: right])
        elif not brackets:
            if c == 'x':
                values[-1] += 1
            elif c == '|':
                values.append(0)
    return max(values)

print(get_max_length(reg))
