# Hashtables
 is a data structure that implements an associative array abstract data type, a structure that can map keys to values

## Challenge
Implement a Hashtable Class with the following methods:

- add
- get
- contains
- hash

## Approach & Efficiency
 ![bigo](https://miro.medium.com/max/875/1*W4_MJgwQTobJFs8nS4wyVQ.png)

 In terms of manipulating dataset, such as lookup, insertion, deletion, and search, Hash tables have huge advantage since it has key — value-based structure. If every element is where it should be the search can use a single comparison to discover the presence of an element. It means that searching for the element takes the same amount of time as searching for the first element of an array, which is a constant time or O(1). However, if our dataset is bigger than the hash table collisions occur and we need to deal with them using different methods. It takes also constant time to insert and delete an element because the hash function determines where to save or remove it.


## API
 add
 1. Arguments: key, value
 2. Returns: nothing
 This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
 get
 1. Arguments: key
 2. Returns: Value associated with that key in the table
 contains
 1. Arguments: key
 2. Returns: Boolean, indicating if the key exists in the table already.
 hash
 1. Arguments: key
 2. Returns: Index in the collection for that key
