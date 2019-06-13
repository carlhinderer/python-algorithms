from src.collection.node import *
import pytest

class TestNode:
    def test_constructor(self):
        node = Node('abc')
        assert node.data == 'abc'
        assert node.next is None

    def test_string_conversion(self):
        node = Node(123)
        assert str(node) == '123'