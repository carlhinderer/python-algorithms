from src.ch06.sequential_search import (
    unordered_sequential_search,
    ordered_sequential_search
    )


def test_unordered_sequential_search():
    assert unordered_sequential_search([1], 1)
    assert unordered_sequential_search([1, 2, 3, 4], 1)

    assert not unordered_sequential_search([], 1)
    assert not unordered_sequential_search([1, 2, 3, 4], 5)


def test_ordered_sequential_search():
    assert ordered_sequential_search([1], 1)
    assert ordered_sequential_search([1, 2, 3, 4], 1)

    assert not ordered_sequential_search([], 1)
    assert not ordered_sequential_search([1, 2, 3, 4], 5)
