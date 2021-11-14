from stack_queue_pseudo import PseudoQueue
import pytest

#@pytest.mark.skip('todo')
def test_PseudoQueue_enqueue():
    expected="[ 1 ] -> Null"
    pesudo_queue = PseudoQueue()
    pesudo_queue.enqueue(1)
    actual = str(pesudo_queue)
    assert expected == actual

# @pytest.mark.skip('todo')
def test_PseudoQueue_multiple_enqueues(pQueue):
    pQueue.enqueue(9)
    expected = "[ 9 ] -> [ 7 ] -> [ 5 ] -> [ 3 ] -> [ 1 ] -> Null"
    actual = str(pQueue)
    assert expected == actual


# @pytest.mark.skip('todo')
def test_PseudoQueue_dequeue(pQueue):
    expected ="[ 7 ] -> [ 5 ] -> [ 3 ] -> Null"
    pQueue.dequeue()
    actual = str(pQueue)
    assert expected == actual


# @pytest.mark.skip('todo')
def test_PseudoQueue_multiple_dequeues(pQueue):
    expected ="[ 7 ] -> [ 5 ] -> Null"
    pQueue.dequeue()
    pQueue.dequeue()
    actual = str(pQueue)
    assert expected == actual

@pytest.fixture
def pQueue():
    pQueue=PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(3)
    pQueue.enqueue(5)
    pQueue.enqueue(7)
    return pQueue
