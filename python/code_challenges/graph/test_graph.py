from graph import Graph, Vertex
import pytest

#@pytest.mark.skip('todo')
def test_graph_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

#@pytest.mark.skip('todo')
def test_graph_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected

#@pytest.mark.skip('todo')
def test_graph_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected

#@pytest.mark.skip('todo')
def test_graph_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

#@pytest.mark.skip('todo')
def test_graph_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

#@pytest.mark.skip('todo')
def test_graph_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected

#@pytest.mark.skip('todo')
def test_graph_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

#@pytest.mark.skip('todo')
def test_breadth_first():
    graph = Graph()

    blue = graph.add_node('blue')
    red = graph.add_node('red')
    yellow = graph.add_node('yellow')
    pink = graph.add_node('pink')

    graph.add_edge(blue,pink)
    graph.add_edge(yellow,pink)
    graph.add_edge(red,yellow)
    graph.add_edge(pink,red)

    expected = 'blue ,pink ,red ,yellow ,'
    actual = graph.breadth_first(blue)
    assert actual == expected

#@pytest.mark.skip('todo')
def test_graph_depth_first():
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)

    graph.add_edge(b,c)
    graph.add_edge(b,d)

    graph.add_edge(c,g)

    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)

    graph.add_edge(f,h)


    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = graph.depth_first(a)
    assert actual == expected
