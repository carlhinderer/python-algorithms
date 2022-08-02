from src.ch04.number_conversion import base_converter, divide_by_2


def test_divide_by_2():
    assert divide_by_2(1) == '1'
    assert divide_by_2(233) == '11101001'


def test_base_converter():
    assert base_converter(25, 2) == '11001'
    assert base_converter(25, 8) == '31'
    assert base_converter(25, 16) == '19'
