from trees import *
from tree_fizz_buzz import *
import pytest
def test_fizz_buzz():
    expected = ['2', 'Fizz', 'FizzBuzz', 'Buzz', '1', 'Fizz', '22']
    tree = BinaryTree
    a_node = Node_(2)
    b_node = Node_(3)
    c_node = Node_(15)
    d_node = Node_(85)
    e_node = Node_(1)
    f_node = Node_(33)
    g_node = Node_(22)
    a_node.child.append( b_node)
    a_node.child.append( c_node)
    a_node.child.append( d_node)
    b_node.child.append( e_node)
    b_node.child.append( f_node)
    c_node.child.append( g_node)
    # Add Root node to tree
    tree.root = a_node
    new_tree = fizz_buzz_tree(tree)
    print( k_ary_bfs(new_tree))
    actual = k_ary_bfs(new_tree)
    assert actual == expected
