from src.ch04.palindrome_checker import pal_checker


def test_pal_checker():
    assert pal_checker('')
    assert pal_checker('a')
    assert pal_checker('abcba')
