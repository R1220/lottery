from num_gen import substitute
from collections import Counter

def rules(list):
    repeat = Counter(list)
    for letter, count in repeat.most_common():
        if count > 2:
            list.remove(letter)
            list.append(substitute(1, 36, letter))

    return list
