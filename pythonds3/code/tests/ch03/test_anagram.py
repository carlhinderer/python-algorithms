import pytest

from src.ch03.anagram import (
    anagram_solution_1,
    anagram_solution_2,
    anagram_solution_4
    )


TEST_CASES = [
    ('', '', True),
    ('a', 'a', True),
    ('apple', 'pleap', True),
    ("abcd", "dcba", True),
    ('', 'a', False),
    ("abcd", "dcda", False)
]


@pytest.mark.parametrize('s1, s2, result', TEST_CASES)
def test_anagram_solution_1(s1, s2, result):
    assert anagram_solution_1(s1, s2) == result


@pytest.mark.parametrize('s1, s2, result', TEST_CASES)
def test_anagram_solution_2(s1, s2, result):
    assert anagram_solution_2(s1, s2) == result


@pytest.mark.parametrize('s1, s2, result', TEST_CASES)
def test_anagram_solution_4(s1, s2, result):
    assert anagram_solution_4(s1, s2) == result
