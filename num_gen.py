import random

def generator(x,y):
    number = random.randint(x, y)
    return number
def substitute(x,y,exclude):
    numbers = list(range(x, y))
    numbers.remove(exclude)
    number = random.choice(numbers)

    return number
