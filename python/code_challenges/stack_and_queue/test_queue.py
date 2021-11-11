from stack_and_queue.queue import Queue
import pytest

def test_queue_enqueue():
    expected=11
    queue=Queue()
    queue.enqueue(11)
    actual=queue.rear.data
    assert expected==actual


def test_queue_enqueue_multi(queue):
    expected=11
    queue.enqueue(11)
    actual = queue.rear.data
    assert expected==actual

def test_queue_dequeue(queue):
    expected = 1
    actual = queue.dequeue()
    assert expected == actual

def test_queue_peek(queue):
    expected = 1
    actual = queue.peek()
    assert expected == actual

def test_queue_empty_after_multi_dequeues(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

def test_queue_empty_instantiate():
    queue = Queue()
    assert queue.front == None

def test_queue_dequeue_from_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.dequeue()

def test_queue_peek_from_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.peek()


@pytest.fixture
def queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)

    return queue

