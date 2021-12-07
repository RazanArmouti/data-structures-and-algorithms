from quick_sort import quick_sort

def test_quick_sort():
    expected = [4, 8, 15, 16, 23, 42]
    list = [8, 4, 23, 42, 16, 15]
    n = len(list)
    actual = quick_sort(list, 0, n-1)
    assert actual == expected
