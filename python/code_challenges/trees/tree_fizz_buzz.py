from trees import *

def fizz_buzz_tree(tree):
    """
    Arguments: k-ary tree
    Return:  new k-ary tree
    """
    queue =Queue()
    queue.enqueue(tree.root)

    while queue.peek():
        front= queue.dequeue()
        front.data=fizz_buzz(front)
        for child in front.child:
            queue.enqueue(child)
    return tree

def fizz_buzz(node):
    if not node.data % 5 and not node.data % 3:
        return "FizzBuzz"
    elif not node.data % 3:
        return "Fizz"
    elif not node.data % 5:
        return "Buzz"
    else:
        return str(node.data)

def k_ary_bfs(tree):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        """
        breadth = Queue()
        breadth.enqueue(tree.root)

        list_of_items = []
        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]
            if front.child:
                for item in front.child:
                    breadth.enqueue(item)
        return list_of_items

if __name__=="__main__":
    pass
