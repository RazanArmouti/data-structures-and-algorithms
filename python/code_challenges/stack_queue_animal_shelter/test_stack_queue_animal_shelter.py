from stack_queue_animal_shelter import AnimalShelter
import pytest

#@pytest.mark.skip('todo')
def test_AnimalShelter_enqueue_cat():
    expected="cat"
    animal=AnimalShelter()
    animal.enqueue("cat")
    actual=animal.cat.rear.data
    assert expected==actual

#@pytest.mark.skip('todo')
def test_AnimalShelter_enqueue_dog():
    expected="dog"
    animal=AnimalShelter()
    animal.enqueue("dog")
    actual=animal.dog.rear.data
    assert expected==actual

#@pytest.mark.skip('todo')
def test_AnimalShelter_enqueue_other():
     with pytest.raises(Exception):
        animal=AnimalShelter()
        animal.enqueue("rabbit")

#@pytest.mark.skip('todo')
def test_AnimalShelter_dequeue_cat():
    expected="cat1"
    animal=AnimalShelter()
    animal.enqueue("cat")
    animal.enqueue("cat1")
    animal.enqueue("cat2")
    animal.dequeue("cat")
    actual=animal.cat.front.data
    assert expected==actual

#@pytest.mark.skip('todo')
def test_AnimalShelter_dequeue_dog():
    expected="dog1"
    animal=AnimalShelter()
    animal.enqueue("dog")
    animal.enqueue("dog1")
    animal.enqueue("dog2")
    animal.dequeue("dog")
    actual=animal.dog.front.data
    assert expected==actual

#@pytest.mark.skip('todo')
def test_AnimalShelter_dequeue_other():
    expected="Null"
    animal=AnimalShelter()
    actual=animal.dequeue("rabbit")
    assert expected==actual
