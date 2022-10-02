from Graph import Graph
from Itinerary import Itinerary
from Graph_Algorithms.Dijkstra import Dijkstra
import itertools
from sys import maxsize
from itertools import permutations


class PatrolPlanner:

    def __init__(self, graph: Graph, nodes_to_visit: list, starting_node):
        self.graph = graph
        self.compressed_graph = Graph()
        self.mst = Graph()
        for node in nodes_to_visit:
            if self.graph.get_node(node) is None:
                raise Exception("Some of the nodes to visit are not contained "
                                "in the graph. Please make sure every node in "
                                "the list is contained in the graph.")
        self.nodes_to_visit = set(nodes_to_visit)
        self.starting_node = starting_node
        self.nodes_to_visit.add(starting_node)
        self.patrol_path = []
        self.condensed_patrol_path = []
        self.patrol_path_weight = 0

    def add_node_to_visit(self, node_id):
        if self.graph.get_node(node_id) is None:
            raise Exception("Node with that id not contained in the Graph.")
        if node_id == self.starting_node or node_id in self.nodes_to_visit:
            pass
        self.nodes_to_visit.add(node_id)

    def tsp(self, graph: Graph, s):
        nodes = list(graph.all_nodes.keys())
        if s in nodes:
            nodes.remove(s)
        possible_paths = permutations(nodes)
        min_path = maxsize
        min_permutation = []
        for permutation in possible_paths:
            current_weight = 0
            permutation = list(permutation)
            permutation = [s] + permutation
            permutation.append(s)
            for i in range(len(permutation)-1):
                itinerary = Itinerary(self.graph, permutation[i],
                                      permutation[i+1], Dijkstra())
                weight = itinerary.find_shortest_path()['travel time']
                current_weight += weight
            min_path = min(min_path, current_weight)
            min_permutation = permutation
        return min_permutation, min_path

    def find_patrol_path(self):
        edge_combinations = list(itertools.combinations(
            self.nodes_to_visit, 2))
        paths_weights = {}
        for edge in edge_combinations:
            itinerary1 = Itinerary(self.graph, edge[0], edge[1], Dijkstra())
            result = itinerary1.find_shortest_path()
            path = list(map(int, result['path']))
            weight = result['travel time']
            paths_weights[edge] = [path, weight]
            self.compressed_graph.add_edge(edge[0], edge[1], weight)

        self.condensed_patrol_path = self.tsp(self.compressed_graph,
                                              self.starting_node)[0]
        for i in range(0, len(self.condensed_patrol_path) - 1):
            condensed_edge = (self.condensed_patrol_path[i],
                              self.condensed_patrol_path[i + 1])
            condensed_edge_rev = (self.condensed_patrol_path[i + 1],
                                  self.condensed_patrol_path[i])
            if condensed_edge in list(paths_weights.keys()):
                for node in paths_weights[condensed_edge][0]:
                    self.patrol_path.append(node)
                self.patrol_path_weight += paths_weights[condensed_edge][1]
            else:
                paths_weights[condensed_edge_rev][0].reverse()
                for node in paths_weights[condensed_edge_rev][0]:
                    self.patrol_path.append(node)
                self.patrol_path_weight += paths_weights[condensed_edge_rev][1]
        for node in self.patrol_path:
            if self.patrol_path.count(node) > 1 and node != self.starting_node:
                self.patrol_path.remove(node)
        return [self.patrol_path, self.patrol_path_weight]

    @staticmethod
    def print_graph_path(path: list, weight: int):
        string_path = list(map(str, path))
        print("Patrol Path:")
        print("Travel time is " + str(weight) + ".")
        print("Stations Traversed")
        print(" --> ".join(string_path))
