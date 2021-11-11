from stack_and_queue import __version__
from stack_and_queue.stack import Stack
import pytest

#@pytest.mark.skip('todo')
def test_version():
    assert __version__=='0.1.0'

# @pytest.mark.skip('todo')
def test_stack_push(stack):
    expected=9
    actual=stack.top.data
    assert expected==actual

# @pytest.mark.skip('todo')
def test_stack_push_multi():
    expected=11
    stack=Stack()
    stack.push(11)
    actual=stack.top.data
    assert expected==actual

# @pytest.mark.skip('todo')
def test_stack_pop(stack):
    expected = 9
    actual = stack.pop()
    assert expected == actual

# @pytest.mark.skip('todo')
def test_stack_pop_all(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True

# @pytest.mark.skip('todo')
def test_stack_empty():
    stack = Stack()
    assert stack.is_empty() == True

# @pytest.mark.skip('todo')
def test_not_empty_stack(stack):
    assert stack.is_empty() == False

# @pytest.mark.skip('todo')
def test_stack_peek(stack):
    expected=9
    actual=stack.peek()
    assert expected==actual

# @pytest.mark.skip('todo')
def test_stack_peek_next(stack):
    expected=7
    stack.pop()
    actual=stack.peek()
    assert expected==actual

# @pytest.mark.skip('todo')
def test_stack_empty_instantiate():
    stack = Stack()
    assert stack.is_empty() == True

# @pytest.mark.skip('todo')
def test_stack_peek_empty():
    with pytest.raises(Exception):
        stack=Stack()
        stack.peek()

# @pytest.mark.skip('todo')
def test_stack_pop_empty():
    with pytest.raises(Exception):
        stack=Stack()
        stack.pop()


@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.push(9)

    return stack

