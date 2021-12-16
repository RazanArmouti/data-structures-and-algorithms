from hash_table import HashTable
from hashmap_left_join import left_join
import pytest

@pytest.mark.skip('todo')
def test_left_join_hashmap_happy_path():
    first_hash_table = HashTable()
    first_hash_table.add("person", "23")
    first_hash_table.add("person1", "30")
    first_hash_table.add("person2", "27")
    first_hash_table.add("person3", "18")
    first_hash_table.add("person4", "19")
    second_hash_table = HashTable()
    second_hash_table.add("person", "45")
    second_hash_table.add("person1", "25")
    second_hash_table.add("person2", "19")
    second_hash_table.add("person4", "9")

    expected = [
        ['person', '23', '45'],
        ['person1', '30', '25'],
        ['person2', '27', '19'],
        ['person3', '18', None],
        ['person4', '19', '9']
        ]
    actual = left_join(first_hash_table, second_hash_table)
    assert actual == expected

@pytest.mark.skip('todo')
def test_left_join_hashmap_with_first_hashmap_empty():
    first_hash_table = HashTable()
    second_hash_table = HashTable()
    second_hash_table.add("person", "45")
    second_hash_table.add("person1", "25")
    second_hash_table.add("person2", "19")
    second_hash_table.add("person4", "9")

    expected = []

    actual = left_join(first_hash_table, second_hash_table)
    assert actual == expected

@pytest.mark.skip('todo')
def test_left_join_hashmap_with_second_hashmap_empty():
    first_hash_table = HashTable()
    first_hash_table.add("person", "45")
    first_hash_table.add("person1", "25")
    first_hash_table.add("person2", "19")
    first_hash_table.add("person4", "9")
    second_hash_table = HashTable()

    expected = [
        ['person', '45', None],
        ['person1', '25', None],
        ['person2', '19', None],
        ['person4', '9', None]
        ]

    actual = left_join(first_hash_table, second_hash_table)
    assert actual == expected

@pytest.mark.skip('todo')
def test_left_join_hashmap_with_hashmaps_empty():
        first_hash_table = HashTable()
        second_hash_table = HashTable()
        expected = []
        actual = left_join(first_hash_table, second_hash_table)
        assert actual == expected

