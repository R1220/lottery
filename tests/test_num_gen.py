from num_gen import generator

def test_generator():
    result = generator(1, 2)
    assert result == 1 or result == 2
