from draw_ball import ball
from collections import Counter
import collections

def rules():
    list = ball(5)
    c = Counter(list)
    for letter, count in c.most_common(2):
        o = ('%s %7d' % (letter, count))

    return o
