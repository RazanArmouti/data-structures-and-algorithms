from linked_list import *
import pytest
# @pytest.mark.skip('todo')
def test_node_with_int_data():
    expected = 7
    node =Node(7)
    actual = node.value
    assert expected==actual

# @pytest.mark.skip('todo')
def test_node_with_str_data():
    expected ='R'
    node= Node('R')
    actual=node.value
    assert expected==actual
# @pytest.mark.skip('todo')
def test_node_is_Node():
    expected ="Node"
    node=Node(1)
    actual=type(node).__name__
    assert expected==actual

# @pytest.mark.skip('todo')
def test_node_without_value():
    with pytest.raises(TypeError):
        node=Node()

# @pytest.mark.skip('todo')
def test_linkedlist_empty():
    expected=None
    datalist=linkedList()
    actual=datalist.head
    assert expected==actual

# @pytest.mark.skip('todo')
def test_linkedlist_insert_one_Node():
    expected=1
    item=linkedList()
    actual=item.insert(1)

# @pytest.mark.skip('todo')
def test_linkedlist_insert_many_Nodes():
    expected=3
    item=linkedList()
    actual1=item.insert(1)
    actual2=item.insert(2)
    actual3=item.insert(3)

# @pytest.mark.skip('todo')
def test_linkedlist_found():
    expected=True
    findItem=linkedList()
    findItem.insert(7)
    actual=findItem.__contains__(7)
    assert expected==actual

# @pytest.mark.skip('todo')
def test_linkedlist_not_found():
    expected=False
    findItem=linkedList()
    findItem.insert(9)
    findItem.insert(2)
    findItem.insert(7)
    actual=findItem.__contains__(1)
    assert expected==actual
# @pytest.mark.skip('todo')
def test_str_all_values():
    expected = "{ a } -> { b } -> { c } -> NULL"
    item=linkedList()
    item.insert('a')
    item.insert('b')
    item.insert('c')
    actual=item.__str__()
    print("final "+ actual)
    assert expected==actual




