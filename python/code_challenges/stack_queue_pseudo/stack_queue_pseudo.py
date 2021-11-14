from stack_and_queue.stack import Stack


class PseudoQueue:
    """
    class will implement standard queue using Stack class
    """
    def __init__(self):
        self.front=None
        self.rear=None
        self.stack_1=Stack()
        self.stack_2=Stack()

    def enqueue(self,value):
        """
        This method inserts value into the PseudoQueue, using a first-in, first-out approach.
        arguments: value
        return :None
        """
        self.stack_1.push(value)
        self.rear=self.stack_1.top.data


    def dequeue(self):
        """
        This method Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        arguments: None
        return: the poped node value
        """
        if self.stack_1.top:
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

            popedValue=self.stack_2.pop()
            self.front=self.stack_2.top
            self.stack_1=Stack()
            while not self.stack_2.is_empty():
                self.stack_1.push(self.stack_2.pop())

            return popedValue
        else:
            raise Exception("queue is empty")

    def __str__(self):
        """
        This method to print out the queue
        Arguments -> none
        return -> the queue
        """
        queue=''
        current=self.stack_1.top
        while current:
            queue+="[ "+str(current.data)+" ] -> "
            current=current.next
        queue+='Null'
        return queue


if __name__=="__main__":
    pQueue=PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(3)
    pQueue.enqueue(5)
    pQueue.enqueue(7)

    print(str(pQueue))
    print(pQueue.rear)
    pQueue.dequeue()
    print(str(pQueue))
    print(pQueue.front)

