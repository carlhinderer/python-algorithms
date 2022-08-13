from src.ch06.binary_search import binary_search, binary_search_rec

import pytest


@pytest.fixture()
def empty_list():
    return []


@pytest.fixture()
def one_item_list():
    return [1]


@pytest.fixture()
def many_items_list():
    return [0, 1, 2, 8, 13, 17, 19, 32, 42]


def test_binary_search(empty_list, one_item_list, many_items_list):
    assert binary_search(one_item_list, 1)
    assert binary_search(many_items_list, 17)

    assert not binary_search(empty_list, 1)
    assert not binary_search(many_items_list, 18)


def test_binary_search_rec(empty_list, one_item_list, many_items_list):
    assert binary_search_rec(one_item_list, 1)
    assert binary_search_rec(many_items_list, 17)

    assert not binary_search_rec(empty_list, 1)
    assert not binary_search_rec(many_items_list, 18)
