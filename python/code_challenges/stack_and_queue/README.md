# Stacks and Queues
A **stack** is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

A **Queue** is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO)

## Challenge
Implement both Stack and a Queue

**Stack**: Create a Stack class that has a top property. It creates an empty Stack when instantiated.

* push
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.
* pop
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    Should raise exception when called on empty stack
* peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
   - Should raise exception when called on empty stack
* is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.

**Queue**: Create a Queue class that has a front property. It creates an empty Queue when instantiated.

* enqueue
    - Arguments: value
    - adds a new node with that value to the back of - the queue with an O(1) Time performance.
* dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
* peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty stack
* is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty

## Approach & Efficiency
I use classes to implement both stack and queue
**Queue :**

* enqueue - O(1)
* dequeue - O(1)
* peek - O(1)
* is empty - O(1)

**Stack :**
* push - O(1)
* pop - O(1)
* peek - O(1)
* is empty - O(1)

## API
 ### Queue :

 ```python
 class Queue:
    """
    class will implement the Queue data structure

    Attribute:
    front -> the first Node of the queue.
    rear ->  the last Node of the queue.

    Methods:
    enqueue() -> add node to the queue
        arguments -> value
        return -> none

    dequeue () -> remove node from the queue
        arguments -> none
        return -> the poped node value

    peek() -> view the value of the front Node in the queue
        arguments ->none
        return -> top node value

    is_empty() ->
        arguments -> none
        return -> True if the queue empty , False if not

    """
```

### Stack :

```python
class Stack:
    """
    class will implement the Stack data structure

    Attribute:
    top ->  the top of the stack.

    Methods:
    push() -> add node to stack
        arguments -> value
        return -> none

    pop() -> remove node from stack
        arguments -> none
        return -> the poped node value

    peek() -> view the top value
        arguments ->none
        return -> top node value

    is_empty() ->
        arguments -> none
        return -> True if the stack empty , False if not

    """

```
