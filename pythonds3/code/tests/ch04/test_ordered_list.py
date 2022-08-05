from src.ch04.ordered_list import OrderedList


def test_ordered_list_creation():
    OrderedList()


def test_list_is_empty():
    o = OrderedList()
    assert o.is_empty()

    o.add('abc')
    assert not o.is_empty()

    o.remove('abc')
    assert o.is_empty()


def test_list_add_remove():
    o = OrderedList()
    o.add('abc')
    assert o.size() == 1

    o.remove('abc')
    assert o.size() == 0


def test_list_size():
    o = OrderedList()
    assert o.size() == 0

    o.add('abc')
    assert o.size() == 1

    o.remove('abc')
    assert o.size() == 0


def test_list_search():
    o = OrderedList()
    o.add('abc')

    assert o.search('abc')
    assert not o.search('def')
