from src.collection.singly_linked_list import *
import pytest

class TestSinglyLinkedList:

    def test_constructor(self):
        l = SinglyLinkedList()
        assert l.head is None
        assert l.tail is None
        assert l.count == 0

    def test_append(self):
        l = SinglyLinkedList()

        # Empty list
        l.append('abc')
        assert l.head.data == 'abc'
        assert l.tail.data == 'abc'
        assert l.count == 1

        # Nonempty list
        l.append('def')
        assert l.head.data == 'def'
        assert l.tail.data == 'abc'
        assert l.count == 2

    def test_iterator(self):
        l = SinglyLinkedList()
        l.append('abc')
        l.append('def')

        data_list = [data for data in l.iter()]
        assert data_list == ['abc', 'def']

    def test_delete(self):
        l = SinglyLinkedList()
        l.append('abc')

        l.delete('abc')
        assert l.tail is None
        assert l.count == 0

    def test_search(self):
        l = SinglyLinkedList()
        l.append('abc')

        assert l.search('abc') == True
        assert l.search('def') == False

    def test_clear(self):
        l = SinglyLinkedList()
        l.append('abc')
        l.clear()

        assert l.head is None
        assert l.tail is None
        assert l.count == 0