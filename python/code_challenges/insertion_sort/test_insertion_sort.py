from insertion_sort import __version__
from insertion_sort.insertion_sort import insertionSort
import pytest

# @pytest.mark.skip('todo')
def test_version():
    assert __version__=='0.1.0'

# @pytest.mark.skip('todo')
def test_insertion_sort_first_case():
    expected=[-1,0,6,7,10,20]
    arr=[6,7,10,-1,0,20]
    actual=insertionSort(arr)
    assert actual==expected

# @pytest.mark.skip('todo')
def test_insertion_sort_second_case():
    expected=[3,3,3,5,5,10]
    arr=[5,10,3,5,3,3]
    actual=insertionSort(arr)
    assert actual==expected

# @pytest.mark.skip('todo')
def test_insertion_sort_third_case():
    expected=[3,5,7,9,11]
    arr=[3,5,7,11,9]
    actual=insertionSort(arr)
    assert actual==expected
