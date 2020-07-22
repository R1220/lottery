import random
from random import choice

def generator(x,y):
    number = random.randint(x, y)
    return number
def substitute(x,y,exclude):
    numbers = choice( i for i in range(x, y) if i not in exclude)
    return numbers
