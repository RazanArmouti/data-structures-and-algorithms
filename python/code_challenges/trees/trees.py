"""
This Module defines a Node and a Binary Tree

"""
class Node:
    """
    properties:
    1. value
    2. left child node
    3. right child node

    """
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Queue:
    def __init__(self,collection=[]):
        self.data=collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self,value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

class BinaryTree:
    """
    methods:
    1. pre order
    2. in order
    3. post order : returns an array of the values, ordered appropriately
    """
    def __init__(self):
        self.root=None

    def bfs(self):
        """
        returns a list of items that it contains
        arguments: None
        return: tree items
        """
        q1 = Queue()
        q1.enqueue(self.root)
        list_of_items=[]
        while q1.peek():
            front=q1.dequeue()
            list_of_items+=[front.data]

            if front.left:
                q1.enqueue(front.left)

            if front.right:
                q1.enqueue(front.right)

        return list_of_items

    def pre_order(self):
        list_of_items = []
        def _traversal(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    _traversal(node.left)
                if node.right:
                    _traversal(node.right)

        _traversal(self.root)
        return list_of_items

    def in_order(self):
        list_of_items = []
        def _traversal(node):
            if node:
                if node.left:
                    _traversal(node.left)
                list_of_items.append(node.data)
                if node.right:
                    _traversal(node.right)

        _traversal(self.root)
        return list_of_items

    def post_order(self):
        list_of_items = []
        def _traversal(node):
            if node:
                if node.left:
                    _traversal(node.left)
                if node.right:
                    _traversal(node.right)
            list_of_items.append(node.data)

        _traversal(self.root)
        return list_of_items



class BinarySearchTree(BinaryTree):
    """
    methods:

    1. Add : Adds a new node with that value in the correct location in the binary search tree.
    arguments : value
    return : none

    2. Contains:
    argument: value
    return: True/False
    """
    def __init__(self):
        super().__init__()

    def add(self,value):
        if not self.root:
            self.root= Node(value)
        else :
            temp = self.root
            while temp:
                if value < temp.data:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right

    def __contains__(self,value):
        if not self.root:
            raise Exception("Empty Tree !!!")
        else:
            temp = self.root
            while temp:
                if temp.data == value:
                    return True
                elif temp.data > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right

