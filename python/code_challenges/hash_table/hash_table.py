class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Arguments: key
        Returns: Index in the collection for that key
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

        Arguments: key, value
        Returns: nothing
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Arguments: key
      Returns: Value associated with that key in the table
      """
      # calculate index
      index = self.__hash(key)
      # check if there is a non empty bucket at the index
      if self.__buckets[index]:
        # iterate over linked list
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          # check if the key in each node matches
          if current.value[0] == key:
            # return the value of the node with the mathcing key
            return current.value[1]
          current = current.next

      # return None
      return None

    def contains(self, key):
        """
       Arguments: key
       Returns: Boolean, indicating if the key exists in the table already.
        """
              # calculate index
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self.__buckets[index]:
        # iterate over linked list
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                # check if the key in each node matches
                if current.value[0] == key:
                # return True
                    return True
                    current = current.next

        # return False
        return False

if __name__=="__main__":
    pass
