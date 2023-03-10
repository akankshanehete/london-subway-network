from Graph_Algorithms.ConnectedComponents import ConnectedComponents
from Graph import Graph
from Station_Node import Station_Node
from itertools import combinations
'''
Given a subway graph, this class will return all the
transportation islands present in the network and all the stations
contained in the given transportation island.
It also returns information on how the transportation islands are
connected to each other.
'''

ID = int
Station = Station_Node


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

    # identifies edges that are interzone
    # adds them to a list for deletion
    def identify_interzone_edges(self, node_id: ID):
        self.marked[node_id] = True
        for adjacent in self.graph.get_node(node_id).get_adjacents():
            if self.graph.get_node(node_id).zone != adjacent.zone and \
                    [adjacent.get_node_id(), node_id] not in \
                    self.deletion_edges:
                self.deletion_edges.append([node_id, adjacent.get_node_id()])
            if self.marked[adjacent.get_node_id()] is False:
                self.identify_interzone_edges(adjacent.get_node_id())

    # deletes interzone edges in the graph and stores as a new graph
    # connected components are collected using dfs
    def get_transportation_islands(self):
        self.identify_interzone_edges(self.start)
        for edge in self.deletion_edges:
            self.island_graph.delete_edge(edge[0], edge[1])
        connected_comp = ConnectedComponents()
        trans_islands = connected_comp.\
            get_connected_components(self.island_graph)
        for island in trans_islands:
            self.transport_list.append(island)
            self.transport_list_zones.append(
                self.graph.get_node(island[0]).zone)
        for island in combinations(trans_islands, 2):
            for edge in self.deletion_edges:
                if edge[0] in island[0]:
                    if edge[1] in island[1]:
                        self.transport_islands.add_edge(
                            self.transport_list.index(island[0]),
                            self.transport_list.index(island[1]))
        values = [self.transport_list,
                  self.transport_islands,
                  self.transport_list_zones]
        return values

    # prints summary of transportation islands
    def print_trans_island_summary(self):
        print('Transportation Islands and Zones:')
        for island in self.transport_list:
            print('\nIsland: '+str(island) + ': --> Zone: ' +
                  str(self.transport_list_zones
                      [self.transport_list.index(island)]))
            print('Connected to: ')
            temp = self.transport_list.index(island)
            list_node = self.transport_islands.get_node(temp)
            if list_node is None:
                print("This transportation island is not "
                      "connected to other islands.")
            else:
                for adj in list_node.get_adjacents():
                    print(self.transport_list[adj.get_node_id()])
