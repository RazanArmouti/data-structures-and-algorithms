from trees import *
from tree_breadth_first import *
import pytest

def test_breadth_first():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for A,B,C,D
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["A", "B", "C", "D"]
    # set actual to return value of bfs call
    actual = tree_breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected

def test_breadth_first_2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for A,B,C,D
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree_breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected

