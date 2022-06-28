import pytest

from src.ch01.fraction import Fraction, NonIntegerFractionError


def test_initialization():
    f = Fraction(2, 4)
    assert f.get_num() == 1
    assert f.get_den() == 2

def test_integers():
    with pytest.raises(NonIntegerFractionError):
        f = Fraction(0.5, 2)
    with pytest.raises(NonIntegerFractionError):
        f = Fraction(2, 'abc')

def test_negative_fraction_initialization():
    f1 = Fraction(-1, 3)
    f2 = Fraction(1, -3)
    f3 = Fraction(-1, -3)

    assert f1.get_num() == -1 and f1.get_den() == 3
    assert f2.get_num() == -1 and f2.get_den() == 3
    assert f3.get_num() == 1 and f3.get_den() == 3

def test_nonzero_denominator():
    with pytest.raises(ZeroDivisionError):
        f = Fraction(2, 0)

def test_get_num():
    f = Fraction(1, 4)
    assert f.get_num() == 1

def test_get_den():
    f = Fraction(1, 4)
    assert f.get_den() == 4

def test_equality():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    f3 = Fraction(2, 4)
    f4 = Fraction(3, 4)

    assert f1 == f2
    assert f1 == f3
    assert f1 != f4

def test_comparison_operators():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    f3 = Fraction(2, 3)

    assert f2 > f1
    assert f2 >= f3
    assert f1 < f2
    assert f2 <= f3

def test_str():
    f1 = Fraction(1, 4)
    assert str(f1) == '1/4'

def test_repr():
    f1 = Fraction(1, 4)
    assert repr(f1) == 'Fraction: Num 1/Den 4'

def test_add():
    f1 = Fraction(1, 4)
    f2 = Fraction(1, 4)
    assert f1 + f2 == Fraction(1, 2)

def test_sub():
    f1 = Fraction(2, 3)
    f2 = Fraction(1, 6)
    assert f1 - f2 == Fraction(1, 2)

def test_mul():
    f1 = Fraction(2, 3)
    f2 = Fraction(1, 6)
    assert f1 * f2 == Fraction(1, 9)

def test_truediv():
    f1 = Fraction(2, 3)
    f2 = Fraction(1, 6)
    assert f1 / f2 == Fraction(4, 1)