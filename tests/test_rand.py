from num_gen import generator

def test_gen_test():
    result = generator(1, 2)
    assert result == 1 or result == 2
