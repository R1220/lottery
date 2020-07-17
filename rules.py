from draw_ball import ball
from collections import Counter

def rules():
    list = ball(5)
    count = Counter(list)

    return list, count





## Rules allow duplicate numbers but not if more than 2.
## 3 equal numbers not allowed
## 1,2,3,4,5 OK
## 1,1,2,2,5 OK
## 1,1,1,2,3 NO OK
