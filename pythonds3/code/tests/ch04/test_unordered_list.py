from src.ch04.unordered_list import Node, UnorderedList


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


def test_list_creation():
    UnorderedList()


def test_list_is_empty():
    u = UnorderedList()
    assert u.is_empty()

    u.add('abc')
    assert not u.is_empty()

    u.remove('abc')
    assert u.is_empty()


def test_list_add_remove():
    u = UnorderedList()
    u.add('abc')
    assert u.size() == 1

    u.remove('abc')
    assert u.size() == 0


def test_list_size():
    u = UnorderedList()
    assert u.size() == 0

    u.add('abc')
    assert u.size() == 1

    u.remove('abc')
    assert u.size() == 0


def test_list_search():
    u = UnorderedList()
    u.add('abc')

    assert u.search('abc')
    assert not u.search('def')
