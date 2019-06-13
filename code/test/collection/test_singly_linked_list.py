from src.collection.singly_linked_list import *
from src.collection.node import *
import pytest

class TestSinglyLinkedList:

    def test_constructor(self):
        l = SinglyLinkedList()
        assert l.head is None
        assert l.tail is None
        assert l.count == 0

    def test_append(self):
        node1 = Node('abc')
        node2 = Node('def')
        l = SinglyLinkedList()

        # Empty list
        l.append(node1)
        assert str(l.head) == str(node1)
        assert str(l.tail) == str(node1)
        assert l.count == 1

        # Nonempty list
        l.append(node2)
        assert str(l.head) == str(node2)
        assert str(l.tail) == str(node1)
        assert l.count == 2

    def test_iterator(self):
        node1 = Node('abc')
        node2 = Node('def')
        l = SinglyLinkedList()
        l.append(node1)
        l.append(node2)

        data_list = [str(data) for data in l.iter()]
        assert data_list == ['abc', 'def']

    def test_delete(self):
        assert 0 == 0

    def test_search(self):
        assert 0 == 0


    def test_clear(self):
        assert 0 == 0