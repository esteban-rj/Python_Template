from src.np_calc.np_operations import get_mean, get_max, get_min, get_sum

def test_get_mean():
    assert get_mean([1, 2, 3, 4, 5]) == 3

def test_get_max():
    assert get_max([1, 2, 3, 4, 5]) == 5

def test_get_min():
    assert get_min([1, 2, 3, 4, 5]) == 1

def test_get_sum():
    assert get_sum([1, 2, 3, 4, 5]) == 15

