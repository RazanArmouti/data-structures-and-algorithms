# Trees
<!-- Short summary or background information -->

## Challenge
- Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

- Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:

    - pre order
    - in order
    - post order which returns an array of the values, ordered appropriately.


-  Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    - Add
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
    - Contains
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
class Approach and helper function inside a function to do the recersive staff

- pr_order() -> time: O(log(n)) -- space : O(n)
- in_order() -> time: O(log(n)) -- space : O(n)
- post_order() -> time: O(log(n)) -- space : O(n)
- BFS() -> time: O(n) -- space : O(n)
- add() -> time: O(n) -- space :O(1)
- conatins() -> time: O(n) -- space :O(1)

