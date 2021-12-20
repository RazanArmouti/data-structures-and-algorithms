from graph import Graph, Vertex
from graph_business_trip import business_trip
import pytest

#@pytest.mark.skip('todo')
def test_business_trip():

    graph = Graph()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstropolis = graph.add_node('Monstropolis')
    naboo = graph.add_node('Naboo')
    narnia = graph.add_node('Narnia')

    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(metroville,pandora,82)

    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(arendelle,monstropolis,42)
    graph.add_edge(monstropolis,arendelle,42)

    graph.add_edge(monstropolis,metroville,105)
    graph.add_edge(metroville,monstropolis,105)
    graph.add_edge(monstropolis,naboo,73)
    graph.add_edge(naboo,monstropolis,73)

    graph.add_edge(metroville,naboo,26)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(narnia,metroville,37)

    graph.add_edge(naboo,narnia,250)
    graph.add_edge(narnia,naboo,250)

    assert [True, "$82"] == business_trip(graph,[metroville, pandora])
    assert [True, '$115'] == business_trip(graph,[arendelle,monstropolis, naboo])
    assert [False, "$0"] == business_trip(graph,[naboo, pandora])
    assert [False, '$0'] == business_trip(graph,[narnia, arendelle,naboo])
