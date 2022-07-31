from src.ch04.stack import Stack


def test_stack_creation():
    s = Stack()

def test_is_empty():
    s = Stack()
    assert s.is_empty()

    s.push('abc')
    assert not s.is_empty()

def test_push_and_pop():
    s = Stack()
    s.push('abc')
    s.push('def')
    s.push('ghi')

    assert s.pop() == 'ghi'
    assert s.pop() == 'def'
    assert s.pop() == 'abc'

def test_peek():
    s = Stack()
    s.push('abc')
    assert s.peek() == 'abc'

def test_size():
    s = Stack()
    assert s.size() == 0

    s.push('abc')
    assert s.size() == 1

    s.pop()
    assert s.size() == 0
