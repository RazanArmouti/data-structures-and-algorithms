"""
Test binary tree class
"""
# from trees import __version__
from trees import *
import pytest

from trees import BinarySearchTree, BinaryTree

# def test_version():
#     assert __version__ == '0.1.0'

def test_tree_bfs(tree_2):
    expected = ["A", "B", "C", "D"]
    actual = tree_2.bfs()
    assert actual == expected
    print("test_bfs passed")

def test_tree_bfs_2(tree_3):
    expected = ["1", "2", "3", "4"]
    actual = tree_3.bfs()
    assert actual == expected
    print("test_bfs_2 passed")

def test_tree_pre_order(tree_3):

    expected = ["1", "2", "4", "3"]
    actual = tree_3.pre_order()
    assert actual == expected
    print("test_pre_order_ passed")

def test_tree_post_order(tree_3):
    expected = ["4", "2", "3", "1"]
    actual = tree_3.post_order()
    assert actual == expected
    print("test_post_order_ passed")

def test_tree_in_order(tree_3):
    expected = ["4", "2", "1", "3"]
    actual = tree_3.in_order()
    assert actual == expected
    print("test_in_order_ passed")

def test_tree_empty_tree():
    expected = None
    tree = BinaryTree()
    actual = tree.root

    assert expected == actual

def test_tree_with_single_node():
    expected = "A"
    tree = BinaryTree()
    a_node = Node('A')
    tree.root = a_node
    actual = tree.root.data

    assert actual == expected

# ******************** binary search tree tests **********************
def test_tree_add_once():
    tree = BinarySearchTree()
    tree.add('A')
    expected = "A"
    actual = tree.root.data
    assert actual == expected

def test_tree_add_twice():
    tree = BinarySearchTree()
    tree.add("A")
    tree.add("B")
    expected = ["A","B"]
    actual = tree.pre_order()
    assert actual == expected

def test_tree_contains_value(tree_1):
    expected = True
    actual = tree_1.__contains__("B")
    assert actual == expected

def test_tree_not_contains_value(tree_1):
    expected = False
    actual = tree_1.__contains__("E")
    assert actual == expected

def test_tree_search_in_empty_tree():
   with pytest.raises(Exception):
       tree = BinarySearchTree()
       actual = tree.__contains__("O")

def test_tree_add_left_and_right_nodes(tree_1):
    expected = ["A","B","C"]
    actual = tree_1.pre_order()
    assert actual == expected

#------------ test tree_max method------------------
#@pytest.mark.skip("todo")
def test_tree_max_happy_path(tree_4):
    expected=16
    actual=tree_4.tree_max()
    assert expected==actual

#@pytest.mark.skip("todo")
def test_tree_max_empty_tree():
    with pytest.raises(Exception):
        tree=BinaryTree()
        actual=tree.get_max()

#@pytest.mark.skip("todo")
def test_tree_max_only_root():
    expected=1
    tree=BinarySearchTree()
    tree.add(1)
    actual=tree.tree_max()
    assert expected==actual

#---------------------fixture---------------------------

@pytest.fixture
def tree_1():
    tree = BinarySearchTree()
    tree.add("A")
    tree.add("B")
    tree.add("C")
    return tree

@pytest.fixture
def tree_2():
    tree = BinaryTree()
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    return tree

@pytest.fixture
def tree_3():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    return tree

@pytest.fixture
def tree_4():
    tree=BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(1)
    tree.add(16)
    return tree


