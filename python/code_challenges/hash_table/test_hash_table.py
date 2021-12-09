from hash_table import HashTable
import pytest


@pytest.fixture
def hashtable():
	return HashTable()


def test_hash_table_hash(hashtable):
	expected = 798
	actual = hashtable._HashTable__hash("r")
	assert actual == expected


def test_hash_table_hash_word(hashtable):
	expected = 376
	actual = hashtable._HashTable__hash("dd")
	assert actual == expected


def test_hash_table_add(hashtable):
    expected = "33"
    hashtable.add("razan","33")
    actual = hashtable.get("razan")
    assert actual == expected

def test_hash_table_get(hashtable):
    expected = "Python"
    hashtable.add("JS","Python")
    actual = hashtable.get("JS")
    assert actual == expected

def test_hash_table_get_null(hashtable):
    expected = None
    actual = hashtable.get("flower")
    assert actual == expected

def test_hash_table_handle_collision(hashtable):
    expected = "33"
    hashtable.add("razan","23")
    hashtable.add("razan","33")
    actual = hashtable.get("razan")
    assert actual == expected

def test_hash_table_get_value_within_collision(hashtable):
    expected = "33"
    hashtable.add("razan","23")
    hashtable.add("razan","33")
    actual = hashtable.get("razan")
    assert actual == expected
