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

#@pytest.mark.skip('todo')
def test_insert_before_first_node():
    expected="{ 1 } -> { 2 } -> { 3 } -> NULL"
    ll = linkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert_before(2,1)
    actual= ll.__str__()
    assert actual==expected

#@pytest.mark.skip('todo')
def test_insert_before_middle_node():
    expected ="{ 5 } -> { 1 } -> { 3 } -> NULL"
    ll = linkedList()
    ll.insert(5)
    ll.insert(3)
    ll.insert_before(3,1)
    actual= str(ll)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_insert_before_empty_list():
    expected ="NULL"
    ll = linkedList()
    ll.insert_before(7,1)
    actual= str(ll)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_insert_after_list_empty():
    expected =None
    ll = linkedList()
    actual= ll.insert_after(3,7)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_insert_after_middle_node():
    expected ="{ 5 } -> { 10 } -> { 17 } -> NULL"
    ll = linkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert_after(10,17)
    actual= str(ll)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_insert_after():
    expected ="{ 5 } -> { 17 } -> { 10 } -> { 20 } -> NULL"
    ll = linkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(20)
    ll.insert_after(5,17)
    actual= str(ll)
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

#@pytest.mark.skip('todo')
def test_zipLists():
    expected='{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> NULL'
    ll =linkedList()
    ll2 =linkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)
    ll2.insert(8)
    actual=zipLists(ll,ll2)
    assert actual==expected

#@pytest.mark.skip('todo')
def test_zipLists_empty_lists():
     # Arrange
    excepted='There is no lists to zip'
     # Act
    first_ll =linkedList()
    second_ll =linkedList()
    actual=zipLists(first_ll,second_ll)
    #Assert
    assert excepted==actual

#@pytest.mark.skip('todo')
def test_first_list_empty():
     # Arrange
    excepted="{ 5 } -> { 3 } -> { 2 } -> NULL"
     # Act
    first_ll =linkedList()
    second_ll =linkedList()
    second_ll.insert(5)
    second_ll.append(3)
    second_ll.append(2)
    actual= zipLists(first_ll,second_ll)
    #Assert
    assert excepted==actual

def test_second_list_empty():
     # Arrange
    excepted="{ 5 } -> { 3 } -> { 2 } -> NULL"
     # Act
    first_ll =linkedList()
    second_ll =linkedList()
    first_ll.insert(5)
    first_ll.append(3)
    first_ll.append(2)
    actual= zipLists(first_ll,second_ll)
    #Assert
    assert excepted==actual

#@pytest.mark.skip('todo')
def test_zipLists_second_LL_longer():
    expected='{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 10 } -> { 12 } -> NULL'
    ll =linkedList()
    ll2 =linkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)
    ll2.insert(8)
    ll2.insert(10)
    ll2.insert(12)
    actual=zipLists(ll,ll2)
    assert actual==expected
