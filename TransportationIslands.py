from Graph_Algorithms.ConnectedComponents import ConnectedComponents
from Graph import Graph
from Station_Node import Station_Node
from itertools import combinations
'''
Given a subway graph, this class will return all the transportation islands present in the network and all the stations
contained in the given transportation island. It also returns information on how the transportation islands are 
connected to eachother.

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
        self.transport_list = []
        self.transport_list_zones = []

    def identify_interzone_edges(self, node_id):
        self.marked[node_id] = True
        for adjacent in self.graph.get_node(node_id).get_adjacents():
            if self.graph.get_node(node_id).zone != adjacent.zone and [adjacent.get_node_id(), node_id] not in \
                    self.deletion_edges:
                self.deletion_edges.append([node_id, adjacent.get_node_id()])
            if self.marked[adjacent.get_node_id()] is False:
                self.identify_interzone_edges(adjacent.get_node_id())

    def get_transportation_islands(self):
        self.identify_interzone_edges(self.start)
        for edge in self.deletion_edges:
            self.island_graph.delete_edge(edge[0], edge[1])
        connected_comp = ConnectedComponents()
        transp_islands = connected_comp.get_connected_components(self.island_graph)
        for island in transp_islands:
            self.transport_list.append(island)
            self.transport_list_zones.append(self.graph.get_node(island[0]).zone)
        for island in combinations(transp_islands, 2):
            for edge in self.deletion_edges:
                if edge[0] in island[0]:
                    if edge[1] in island[1]:
                        self.transport_islands.add_edge(self.transport_list.index(island[0]), self.transport_list.index(island[1]))
        return self.transport_list, self.transport_islands, self.transport_list_zones

    def print_trans_island_summary(self):
        print('Transportation Islands and Zones:')
        for island in self.transport_list:
            print('\nIsland: '+str(island) + ': --> Zone: ' + str(self.transport_list_zones[self.transport_list.index(island)]))
            print('Connected to: ')
            list_node = self.transport_islands.get_node(self.transport_list.index(island))
            if list_node is None:
                print("This transportation island is not connected to other islands.")
            else:
                for adj in list_node.get_adjacents():
                    print(self.transport_list[adj.get_node_id()])



