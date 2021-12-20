from graph import Graph, Vertex
def business_trip(graph ,city_list):
    cost = 0
    def walk(city_list):
        nonlocal cost
        first_city = city_list.pop(0)
        cities = graph.get_neighbors(first_city)
        v = [city.vertex for city in cities]
        for city in cities:
            if city_list[0] not in v:
                return [False , "$0"]
            if city.vertex in city_list:
                print(city.weight)
                cost += city.weight
                if len(city_list)>1 :
                    walk(city_list)
    walk(city_list)
    if not cost:
        return [False , "$0"]
    return [True , f"${cost}"]
