# 43735

k = int(input())
text = input()

def calc_relation_index(text: str, name1: str, name2: str, k: int):
    indexes_of_name1 = []
    indexes_of_name2 = []
    groups = (
        (name1, indexes_of_name1, indexes_of_name2),
        (name2, indexes_of_name2, indexes_of_name1)
    )

    total = 0
    word = ""
    for i, c in enumerate(text + "\0"):
        if c.isalpha():
            word += c
        elif word:
            threshold = i - k - len(word)
            for this_name, this_indexes, other_indexes in groups:
                if word == this_name:
                    this_indexes.append(i)
                    while other_indexes and other_indexes[0] < threshold:
                        other_indexes.pop(0)
                    total += len(other_indexes)
                    break
            word = ""
    return total

print(calc_relation_index(text, "Alice", "Bob", k))
