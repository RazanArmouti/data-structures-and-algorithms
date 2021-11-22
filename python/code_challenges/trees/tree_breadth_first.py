from trees import *

def tree_breadth_first(tree):
    """
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered
    """
    queue = Queue()
    queue.enqueue(tree.root)
    list_of_items=[]
    while queue.peek():
        front=queue.dequeue()
        list_of_items+=[front.data]

        if front.left:
             queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

    return list_of_items

if __name__=="__main__":
    pass

