import pytest

from src.ch01.fraction import Fraction


def test_initialization():
    f = Fraction(2, 4)
    assert f.get_num() == 1
    assert f.get_den() == 2

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

def test_str():
    f1 = Fraction(1, 4)
    assert str(f1) == '1/4'

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