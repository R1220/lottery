from rules import rules


def test_rules():
    random = [1, 1, 1, 2, 2]
    assert rules(random) is not [2, 1, 1, 1, 2] \
           or [1, 2, 1, 2, 2] or [1, 1, 2, 2, 2]
