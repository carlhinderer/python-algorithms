from src.collection.double_node import DoubleNode
import pytest

class TestDoubleNode:
    def test_constructor(self):
        node = DoubleNode('abc')
        assert node.data == 'abc'
        assert node.prev is None
        assert node.next is None

    def test_string_conversion(self):
        node = DoubleNode(123)
        assert str(node) == '123'