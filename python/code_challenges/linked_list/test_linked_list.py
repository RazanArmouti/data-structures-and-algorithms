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

# @pytest.mark.skip('todo')
def test_append_node():
    expected ="{ 5 } -> { 7 } -> NULL"
    ll = linkedList()
    ll.insert(5)
    ll.append(7)
    actual= ll.__str__()
    assert actual == expected

# @pytest.mark.skip('todo')
def test_append_many_nodes():
    expected ="{ 1 } -> { 2 } -> { 3 } -> NULL"
    ll = linkedList()
    ll.insert(1)
    ll.append(2)
    ll.append(3)
    actual= str(ll)
    assert actual == expected

@pytest.mark.skip('todo')
def test_insert_before_first_node():
    expected="{ 1 } -> { 2 } -> { 3 } -> NULL"
    ll = linkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert_before(2,1)
    actual= ll.__str__()
    assert actual==expected

@pytest.mark.skip('todo')
def test_insert_before_middle_node():
    expected ="{ 5 } -> { 1 } -> { 3 } -> NULL"
    ll = linkedList()
    ll.insert(5)
    ll.insert(3)
    ll.insert_before(3,1)
    actual= str(ll)
    assert actual == expected

@pytest.mark.skip('todo')
def test_insert_before_empty_list():
    expected ="NULL"
    ll = linkedList()
    ll.insert_before(7,1)
    actual= str(ll)
    assert actual == expected

@pytest.mark.skip('todo')
def test_insert_after_list_empty():
    expected ="the linkedlist is empty"
    ll = linkedList()
    ll.insert(3)
    ll.insert(7)
    actual= ll.insert_after(3,7)
    assert actual == expected

@pytest.mark.skip('todo')
def test_insert_after_middle_node():
    expected ="{ 5 } -> { 3 } -> { 1 } -> NULL"
    ll = linkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert_after(5,3)
    actual= str(ll)
    assert actual == expected

@pytest.mark.skip('todo')
def test_insert_after():
    expected ="{ 5 } -> { 1 } -> { 3 } -> NULL"
    ll = linkedList()
    ll.insert(5)
    ll.insert(1)
    actual= ll.insert_after(3,1)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_kthFromEnd_k_greater_length():
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(5)
    assert "Index out of range" in str(exc.value)
    assert exc.type == Exception

#@pytest.mark.skip('todo')
def test_kthFromEnd_k_equal_length():
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(4)
    assert "Index out of range" in str(exc.value)
    assert exc.type == Exception

#@pytest.mark.skip('todo')
def test_kthFromEnd_k_less_zero():
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(-5)
    assert "k must be non-negative number" in str(exc.value)
    assert exc.type == Exception


#@pytest.mark.skip('todo')
def test_kthFromEnd_size_1():
    expected=1
    ll=linkedList()
    ll.insert(1)
    actual=ll.kthFromEnd(0)
    assert actual==expected

#@pytest.mark.skip('todo')
def test_kthFromEnd_happy_path():
    expected=8
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)
    actual=ll.kthFromEnd(2)
    assert actual==expected

