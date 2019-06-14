from src.collection.single_node import SingleNode
import pytest

class TestSingleNode:
    def test_constructor(self):
        node = SingleNode('abc')
        assert node.data == 'abc'
        assert node.next is None

    def test_string_conversion(self):
        node = SingleNode(123)
        assert str(node) == '123'