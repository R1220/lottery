import random

def generator(x,y):
    number = random.randint(x, y)
    return number
def substitute(x,y,exclude):
    numbers = random.randint(x, y)
    return numbers.remove(exclude)
