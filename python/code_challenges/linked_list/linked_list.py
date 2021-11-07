
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

    def append(self,value):
        """
        this method to add nodes in the end of the list
        """
        node=Node(value)
        currentNode=self.head
        if currentNode:
            while currentNode.next:
                currentNode=currentNode.next
            currentNode.next=node
        else:
            self.head=node

    def insert_before(self,value, newValue):
        """
        adds a new node with the given new value immediately before the first node that has the value specified
        """
        currentnode=self.head
        if not currentnode:
            return "NULL"
        while currentnode.next:
            if currentnode.next.value==value:
                newNode=Node(newValue)
                newNode.next=currentnode.next
                currentnode.next=newNode
        currentnode=currentnode.next
        # newNode = Node(newValue)
        # node = self.head
        # if node == None:
        #     return "NULL"
        # else:
        #     found = None
        #     # search nodes
        #     while node:
        #         if node.next == value:
        #             found = True
        #             beforeInsert = node
        #             afterInsert = node.next
        #             beforeInsert.next = newNode
        #             newNode.next = afterInsert # sets new node's next to target node
        #             node = node.next # continues through while loop
        #         else:
        #             node = node.next
            #if found != True:
                #print('Your target node of {} was not found in the list!'.format(newValue))

    def insert_after(self,value,newValue):
        """
        adds a new node with the given new value immediately after the first node that has the value specified
        """
        currentNode=self.head
        if not currentNode.next:
            return 'the linkedlist is empty'
        while currentNode.next:
            if currentNode.value==value:
                newNode=Node(value)
                newNode.next=currentNode.next
                currentNode.next=newNode
        currentNode=currentNode.next
        #pass




if __name__ =="__main__":
    fNode =linkedList()
    fNode.insert(99)
    print(fNode)





