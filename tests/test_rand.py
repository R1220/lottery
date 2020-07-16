from num_gen import generator

def test_generator():
    for i in range(100):
        result = generator(1, 2)
        assert result == 1 or result == 2

