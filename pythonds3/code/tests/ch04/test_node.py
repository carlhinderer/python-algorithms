from src.ch04.node import Node


def test_node_creation():
    n = Node('abc')
    assert n.data == 'abc'


def test_node_set_data():
    n = Node('abc')
    n.data = 'def'
    assert n.data == 'def'


def test_node_next():
    n1 = Node('abc')
    n2 = Node('def')
    n1.next = n2
    assert n1.next == n2


def test_node_str():
    n = Node('abc')
    assert str(n) == 'abc'
