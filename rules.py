from draw_ball import ball
from collections import Counter

def rules():
    list = ball(5)
    count = Counter(list)
    for i in list:
        if list.count(i) > 2:  ## is not the array address but the item! WRONG!
            list.pop(i)
        new_list_len = len(list)
        if new_list_len < 5:
         list.append(ball(5 - new_list_len))

    return list
