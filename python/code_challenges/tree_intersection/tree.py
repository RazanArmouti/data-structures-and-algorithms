"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains in pre_order

        input: None

        output: tree items

        sub method : walk () to make the recursion staff
        """
        list_of_items = []
        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

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
