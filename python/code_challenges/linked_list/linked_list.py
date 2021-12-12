
class Node:
    """
     Its a class that has properties for the value stored in the Node, and a pointer to the next Node.

     Attributes
     ----------

     Methods
     -------
     __init__(value, next_):
     the constructor method for the class, it takes two parameters,

     /e value parameter is the a reference to the data the node will hold,
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
        if self.head is None:
            print("List has no element")
            return

        if value == self.head.value:
            new_node = Node(newValue)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        print(n.next)
        while n.next is not None:
            if n.next.value == value:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node = Node(newValue)
            new_node.next = n.next
            n.next = new_node
        # currentnode=self.head
        # if not currentnode:
        #     return "NULL"
        # while currentnode.next:
        #     if currentnode.next.value==value:
        #         newNode=Node(newValue)
        #         newNode.next=currentnode.next
        #         currentnode.next=newNode
        # currentnode=currentnode.next


    def insert_after(self,value,newValue):
        """
        adds a new node with the given new value immediately after the first node that has the value specified
        """
        if self.head is None:
            print("List has no element")
            return
        n = self.head
        print(n.next)
        while n is not None:
            if n.value == value:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(newValue)
            new_node.next = n.next
            n.next = new_node

        # currentNode=self.head
        # if not currentNode.next:
        #     return 'the linkedlist is empty'
        # while currentNode.next:
        #     if currentNode.value==value:
        #         newNode=Node(value)
        #         newNode.next=currentNode.next
        #         currentNode.next=newNode
        # currentNode=currentNode.next
        #pass

    def kthFromEnd(self,k):
        """
        This method return the node’s value that is k places from the tail of the linked list.
        argument: a number, k, as a parameter.

        """
        current =self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        current = self.head
        if k < 0:
            raise Exception("k must be non-negative number")
        elif k >= length:
            raise Exception('Index out of range')
        value = length-k-1
        for i in range(length):
            if i == value:
                result=current.value
                return result
            current = current.next

def zipLists(list1, list2):
    """
    This function Zip the two linked lists together into one so that the nodes alternate
     between the two lists and return a reference to the head of the zipped list.

    Arguments: 2 linked lists
    Return: Linked List, zipped .

    """
    flist = list1.head
    slist = list2.head

    if not flist and not slist:
        return 'There is no lists to zip'
    elif  not flist :
        return str(list2)
    elif not slist:
        return str(list1)

    ll =linkedList()
    while flist or slist:
        if flist :
         ll.insert(flist.value)
         flist = flist.next
        if slist :
         ll.insert(slist.value)
         slist = slist.next

    return (ll.__str__())




if __name__ =="__main__":
    print("razzan")
    ll =linkedList()
    ll2 =linkedList()
    ll.append(1)
    ll.append(3)
    ll.append(5)
    ll.append(7)
    print(ll.__str__())
    x=ll.kthFromEnd(0)
    print(x)
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)
    ll2.insert(8)
    ll2.insert(10)
    ll2.insert(12)
    y=zipLists(ll,ll2)
    print(y)
    ll.insert_after(3,7)
    print(ll.__str__())
    ll.insert_before(3,5)
    print(ll.__str__())






