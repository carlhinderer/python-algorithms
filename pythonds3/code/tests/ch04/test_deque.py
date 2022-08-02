from src.ch04.deque import Deque


def test_deque_creation():
    Deque()


def test_add_remove_front():
    d = Deque()
    d.add_front('abc')
    d.add_front('def')

    assert d.remove_front() == 'def'


def test_add_remove_rear():
    d = Deque()
    d.add_rear('abc')
    d.add_rear('def')

    assert d.remove_rear() == 'def'


def test_size():
    d = Deque()
    assert d.size() == 0

    d.add_front('abc')
    assert d.size() == 1

    d.remove_rear()
    assert d.size() == 0


def test_is_empty():
    d = Deque()
    assert d.is_empty()

    d.add_front('abc')
    assert not d.is_empty()

    d.remove_rear()
    assert d.is_empty()
