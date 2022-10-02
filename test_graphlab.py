from Graph_builder import Graph_builder
from Graph import Graph
from Csv_reader import Csv_reader
from Metric_Extractor import Metric_Extractor
from Itinerary import Itinerary
from Graph_Algorithms.Dijkstra import Dijkstra
from Graph_Algorithms.A_star import A_star
from PatrolPlanner import PatrolPlanner
from Station_Node import Station_Node
# from Graph_Algorithms.Priority_Queue import PriorityQueue
# import pytest

# build test graph 1
test_graph1 = Graph()
test_graph1.add_edge(1, 2, 2, 'red')
test_graph1.add_edge(1, 6, 1, 'green')
test_graph1.add_edge(1, 5, 3, 'blue')
test_graph1.add_edge(1, 10, 2, 'blue')
test_graph1.add_edge(2, 3, 4, 'red')
test_graph1.add_edge(2, 6, 1, 'green')
test_graph1.add_edge(3, 4, 2, 'red')
test_graph1.add_edge(4, 5, 4, 'purple')
test_graph1.add_edge(4, 7, 2, 'purple')
test_graph1.add_edge(6, 8, 2, 'yellow')
test_graph1.add_edge(8, 9, 3, 'blue')
test_graph1.add_edge(9, 10, 2, 'blue')

# build test graph 2 (london subway graph)
csv_reader = Csv_reader()
test_graph2 = Graph()
graph2 = Graph_builder(csv_reader, test_graph2)
graph2.create_station_nodes('_dataset/london.stations.csv')
graph2.create_connections('_dataset/london.connections.csv')

# build test graph 3
test_graph3 = Graph()
test_graph3.add_edge(0, 2, 20)
test_graph3.add_edge(0, 1, 10)
test_graph3.add_edge(1, 4, 10)
test_graph3.add_edge(1, 3, 50)
test_graph3.add_edge(2, 3, 20)
test_graph3.add_edge(4, 3, 20)
test_graph3.add_edge(4, 5, 1)
test_graph3.add_edge(5, 3, 2)
test_graph3.add_edge(17, 3, 50)
test_graph3.add_edge(12, 17, 50)
test_graph3.add_edge(9, 17, 13)
test_graph3.add_edge(9, 23, 3)
test_graph3.add_edge(5, 30, 47)
test_graph3.add_edge(30, 4, 50)
test_graph3.add_edge(5, 45, 89)
test_graph3.add_edge(30, 3, 1)


def test_extract_csv():
    filename = '_samples/stations_test.csv'
    reader = Csv_reader()
    values = reader.extract_csv(filename)
    assert values == [{'id': '1', 'name': ' "Anna station'},
                      {'id': '2', 'name': ' "Akanksha station'},
                      {'id': '3', 'name': ' "Sebastian station'},
                      {'id': '4', 'name': ' "Eshaan station'}]


def test_dijkstra():
    itinerary = Itinerary(test_graph1, 1, 7, Dijkstra())
    path = itinerary.find_shortest_path()['path']
    traversed = itinerary.find_shortest_path()['stations traversed']
    distance = itinerary.find_shortest_path()['travel time']
    lines = itinerary.find_shortest_path()['lines']
    assert path == ['1', '5', '4', '7']
    assert traversed == 4
    assert distance == 9
    assert lines == ['blue', 'purple', 'purple']


def test_a_star():
    itinerary = Itinerary(test_graph2, 1, 30, A_star())
    path = itinerary.find_shortest_path()['path']
    traversed = itinerary.find_shortest_path()['stations traversed']
    distance = itinerary.find_shortest_path()['travel time']
    lines = itinerary.find_shortest_path()['lines']
    assert path == ['1', '234', '176', '30']
    assert traversed == 4
    assert distance == 7
    assert lines == ['10', '10', '10']


def test_heuristic():
    from_node = Station_Node(1, "from")
    from_node.set_lat(0)
    from_node.set_long(3)
    to_node = Station_Node(2, "to")
    to_node.set_lat(4)
    to_node.set_long(0)
    heuristic = A_star()
    dist = heuristic.distance(from_node, to_node)
    assert dist == 5


def test_same_node():
    itinerary = Itinerary(test_graph1, 1, 1, Dijkstra())
    path = itinerary.find_shortest_path()['path']
    traversed = itinerary.find_shortest_path()['stations traversed']
    distance = itinerary.find_shortest_path()['travel time']
    lines = itinerary.find_shortest_path()['lines']
    assert path == ['1']
    assert traversed == 1
    assert distance == 0
    assert lines == []


def test_station_node():
    station = Station_Node(1, "test station")
    station.set_lat(2)
    station.set_long(3)
    station.set_zone(4)
    station.set_total_lines(5)
    station.set_is_rail(0)
    station.set_disp_name("test")
    assert station.name == "test station"
    assert station.get_node_id() == 1
    assert station.lat == 2
    assert station.long == 3
    assert station.zone == 4
    assert station.total_lines == 5
    assert station.is_rail == 0
    assert station.disp_name == "test"


def test_metric_extractor():
    metric = Metric_Extractor(test_graph1)
    node_count = metric.get_node_count()
    edge_count = metric.get_edge_count()
    degree = metric.get_degree(1)
    avg_degree = metric.get_avg_degree()
    assert node_count == 10
    assert edge_count == 12
    assert degree == 4
    assert avg_degree == 2.4


def test_patrol_planner():
    patrol = PatrolPlanner(test_graph3, [0, 2, 30, 17], 0)
    patrol_path = patrol.find_patrol_path()
    assert patrol_path[0] == [0, 30, 2, 3, 17, 3, 5, 4, 1, 0]
    assert patrol_path[1] == 188
