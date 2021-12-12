from stack_and_queue.node import Node

class Stack:
    """
    class will implement the Stack data structure

    Attribute:

    top ->  the top of the stack.

    Methods:

    push() -> adds a new node with that value to the top of the stack
        arguments -> value
        return -> none

    pop() -> Removes the node from the top of the stack
        arguments -> none
        return -> the value from node from the top of the stack

    peek() -> view the top value
        arguments ->none
        return -> Value of the node located at the top of the stack

    is_empty() ->
        arguments -> none
        return -> True if the stack empty , False if not

    """
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if not self.top:
            raise Exception("You can't pop from Empty Stack !!!")
        else:
            tmp=self.top
            self.top=self.top.next
            tmp.next=None
        return tmp.data

    def peek(self):
        if not self.top:
            raise Exception("You can't peek from Empty Stack !!!")
        else:
            return self.top.data


    def is_empty(self):
        if not self.top:
            return True
        else:
            return False


