
class Node:
    """
     Its a class that has properties for the value stored in the Node, and a pointer to the next Node.

     Attributes
     ----------

     Methods
     -------
     __init__(value, next_):
     the constructor method for the class, it takes two parameters, the value parameter is the a reference to the data the node will hold,
     and the next_

    """

    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    """
    Its a class for creating instances of a Linked List.
     Attributes
     ----------
     head: Node | None

     Methods
     -------
     insert(value: any)
     contains(value: any) -> bool

    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        This function adds a new node with that value to the head of the list
        arguments:
            value : any
            returns: None
        """
        # create new node
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=node

    def __contains__(self,value):
        """
        This method search in the linked list for a given value , and return True if the value exist and return False not exist
        arguments:
            value : any
            returns: True/False
        """
        if self.head==None:
            return False
        else:
            x= self.head
            while x != None:
                if x.value==value:
                    return True
                x=x.next
            return False

    def __str__(self):
        """
        This method print all linkedlist nodes values.
        Arguments: none
        Returns: a string representing all the values in the Linked List, formatted as:"{ a } -> { b } -> { c } -> NULL"

        """
        currentNode=self.head
        formattedNode=''
        while currentNode is not None:
            formattedNode +="{ "+ str(currentNode.value) +" } -> "
            currentNode=currentNode.next

        formattedNode+= "NULL"
        return formattedNode

if __name__ =="__main__":
    fNode =linkedList()
    fNode.insert(99)
    print(fNode)





