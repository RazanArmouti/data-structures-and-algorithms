# Singly Linked List
 linked list is a string of nodes, sort of like a string of pearls, with each node containing both data and a reference to the next node in the list (Note: This is a singly linked list. The nodes in a doubly linked list will contain references to both the next node and the previous node). The main advantage of using a linked list over a similar data structure, like the static array, is the linked list’s dynamic memory allocation: if you don’t know the amount of data you want to store before hand, the linked list can adjust on the fly.* Of course this advantage comes at a price: dynamic memory allocation requires more space and commands slower look up times.

## Challenge
 * Insert: inserts a new node into the list
 * Search: searches list for a node containing the requested data and returns true if found, otherwise return false

## Approach & Efficiency
 time complexity : O(n)
 space complexity :O(1)

## API
 Navigate to python/code_challenges then run poetry install then convert the shell to poetry shell and run pytest
