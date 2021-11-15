from stack_and_queue.queue import Queue
class AnimalShelter:
    """
    This class holds only dogs and cats

    Methods:
    1. enqueue:-
        arguments: animal can be either a dog or a cat object
        return: None

    2. dequeue:-
        arguments: pref can be either "dog" or "cat"
        return: dog or a cat or Null

    """
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()

    def enqueue(self,animal):
        if animal.lower().startswith("cat"):
            self.cat.enqueue(animal)
        elif animal.lower().startswith("dog"):
            self.dog.enqueue(animal)
        else:
            raise Exception("This shelter for cats and dogs only !!!")


    def dequeue(self,pref):
        if pref.lower().startswith("cat"):
            self.cat.dequeue()
        elif pref.lower().startswith("dog"):
            self.dog.dequeue()
        else:
            return "Null"


    if __name__=="__main__":
        pass

