from src.collection.singly_linked_list import *
import pytest

class TestSinglyLinkedList:
    def test_constructor(self):
        l = SinglyLinkedList()
        assert l.head is None
        assert l.tail is None
        assert l.count == 0