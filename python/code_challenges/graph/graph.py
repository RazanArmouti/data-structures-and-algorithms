from collections import deque


class Vertex:
  """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
  def __init__(self, value):
    """
    Initalization for a Vertex to hold a value.

    """
    self.value = value

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class Stack:
  def __init__(self):
    """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
    self.dq = deque()

  def push(self, value):
    """
		Store the passed value in a node and then push the node on top of the stack.

		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
    self.dq.append(value)

  def pop(self):
    """
		Return the top node in a stack.
		"""
    self.dq.pop()

class Edge:
  """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

  """
  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:
    def __init__(self):
        """
        Initalization for a hashmap to hold the vertices
        """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
            Method for Adding a node to the graph
            Arguments: value
            Returns: The added node
        """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        """
        Returns the total number of nodes in the graph

        Returns:
            [int]:
        """
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: All nodes
        """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])

    def breadth_first(self, start_vertex):
        """
        Arguments: Node
        Return: A collection of nodes in the order they were visited.

        """
        queue = Queue()
        visited = set()
        final_result = ''
        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while queue.peek():
            current_vertex = queue.dequeue()
            final_result += f"{current_vertex.value} ,"
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor =  edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return final_result

    def depth_first(self ,start_vertex):
        """
        Arguments: Node (Starting point of search)
        Return: A collection of nodes in their pre-order depth-first traversal order

        """
        list_of_items = []
        list_of_items.append(start_vertex.value)

        def walk(vertex):
            edge =self.__adjacency_list[vertex]
            for v in edge:
                my_vertex = v.vertex.value
                if my_vertex not in list_of_items:
                    list_of_items.append(my_vertex)
                    walk(v.vertex)
        walk(start_vertex)
        return list_of_items



