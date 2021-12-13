from hash_table import HashTable
from tree_intersection import tree_intersection
from tree import BinaryTree
import pytest

#@pytest.mark.skip('todo')
def test_tree_insertion_happy_path():
    expected = [5, 3, 6]
    tree1 = BinaryTree()
    tree1.add(5)
    tree1.add(3)
    tree1.add(2)
    tree1.add(6)
    tree2 = BinaryTree()
    tree2.add(5)
    tree2.add(1)
    tree2.add(3)
    tree2.add(6)
    actual =tree_intersection(tree1, tree2)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_tree_insertion_sad_path():
    expected = "there is no intersection between these trees"
    tree1 = BinaryTree()
    tree1.add(5)
    tree1.add(3)
    tree1.add(2)
    tree1.add(6)
    tree2 = BinaryTree()
    tree2.add(4)
    tree2.add(1)
    tree2.add(8)
    tree2.add(9)
    actual =tree_intersection(tree1, tree2)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_tree_intersection_with_empty_trees():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)

#@pytest.mark.skip('todo')
def test_tree_intersection_with_first_tree_empty():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree1.add(5)
        tree1.add(3)
        tree1.add(2)
        tree1.add(6)
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)

#@pytest.mark.skip('todo')
def test_tree_intersection_with_second_tree_empty():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        tree2.add(5)
        tree2.add(1)
        tree2.add(3)
        tree2.add(6)
        actual = tree_intersection(tree1, tree2)
