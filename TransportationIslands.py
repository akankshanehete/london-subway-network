from Graph_Algorithms.ConnectedComponents import ConnectedComponents
from Graph import Graph
from Station_Node import Station_Node
'''
Given a subway graph, this class will return all the transportation islands present in the network and all the stations
contained in the given transportation island. It also returns information on how the transportation islands are connected to eachother.

'''

class TransportationIslands:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.island_graph = graph
        self.marked = {}
        for node in self.graph:
            self.marked[node.get_node_id()] = False
            self.start = node.get_node_id()
        self.deletion_edges = []
        self.transport_islands = Graph()

    def identify_interzone_edges(self, node_id):
        self.marked[node_id] = True
        for adjacent in self.graph.get_node(node_id).get_adjacents():
            if self.graph.get_node(node_id).zone != adjacent.zone and [adjacent.get_node_id(), node_id] not in self.deletion_edges:
                self.deletion_edges.append([node_id, adjacent.get_node_id()])
            if self.marked[adjacent.get_node_id()] == False:
                self.identify_interzone_edges(adjacent.get_node_id())


    def get_transportation_islands(self):
        self.identify_interzone_edges(self.start)
        for edge in self.deletion_edges:
            self.island_graph.delete_edge(edge[0], edge[1])
        connected_comp = ConnectedComponents()
        islands = connected_comp.get_connected_components(self.island_graph)
        for island in islands:
            new_edge = []
            if edge[0] in island:
                new_edge[0] = islands.index(island)
            if edge[1] in island:
                new_edge[1] = islands.index(island)


        return islands











testgraph = Graph()
one = Station_Node(1, 's')
one.set_zone(1)
four = Station_Node(4, 's')
four.set_zone(1)
three = Station_Node(3, 's')
three.set_zone(1)
two = Station_Node(2, 's')
two.set_zone(1)
five = Station_Node(5, 's')
five.set_zone(2)
six = Station_Node(6, 's')
six.set_zone(2)
seven = Station_Node(7, 's')
seven.set_zone(2)
testgraph.add_node(one)
testgraph.add_node(two)
testgraph.add_node(three)
testgraph.add_node(four)
testgraph.add_node(five)
testgraph.add_node(six)
testgraph.add_node(seven)

testgraph.add_edge(1, 3)
testgraph.add_edge(1, 2)
testgraph.add_edge(1, 4)
testgraph.add_edge(2, 5)
testgraph.add_edge(6, 7)
testgraph.add_edge(5, 6)
testgraph.add_edge(2, 6)

testgraph.print_all_connections()

islands = TransportationIslands(testgraph)

trans_islands = islands.get_transportation_islands()
print(trans_islands)


