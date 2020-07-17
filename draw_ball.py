from num_gen import generator

def ball(n):
    numbers = []
    while len(numbers) < n:
        gen = generator(1, 2)
        numbers.insert(n, gen)

    return numbers



