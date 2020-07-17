from draw_ball import ball

def test_ball():
    x = 5
    a = ball(x)
    assert len(a) == x+1