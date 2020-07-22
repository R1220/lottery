from draw_ball import ball
from num_gen import substitute
from collections import Counter

def rules():
    list = ball(5)

    c = Counter(list)
    for letter, count in c.most_common():
        o = ('%s %7d' % (letter, count))  ##Needed to identify duplicates during debug
        if count > 2:
            list.remove(letter)
            list.extend(substitute(1, 4, letter))

    return list
