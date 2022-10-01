from Graph import Graph
from Graph_Algorithms.Priority_Queue import PriorityQueue
from Itinerary import Itinerary
from Graph_Algorithms.Dijkstra import Dijkstra
import itertools


class Patrol_Planner:

    def __init__(self, graph: Graph, nodes_to_visit: list, starting_node):
        self.graph = graph
        self.compressed_graph = Graph()
        self.mst = Graph()
        for node in nodes_to_visit:
            if self.graph.get_node(node) is None:
                raise Exception("Some of the nodes to visit are not contained in the graph. Please make sure every node in the list is contained in the graph.")
        self.nodes_to_visit = set(nodes_to_visit)
        self.starting_node = starting_node
        self.nodes_to_visit.add(self.starting_node)
        self.pq = PriorityQueue()
        self.marked = {}
        self.condensed_patrol_path = []
        self.patrol_path = []
        self.patrol_path_weight = 0
        for node in self.graph:
            self.marked[node.get_node_id()] = False

    def add_node_to_visit(self, node_id):
        if self.graph.get_node(node_id) is None:
            raise Exception("Node with that id not contained in the Graph.")
        if node_id == self.starting_node or node_id in self.nodes_to_visit:
            pass
        self.nodes_to_visit.add(node_id)

    def __visit(self, node_id):
        self.marked[node_id] = True
        for adjacent in self.compressed_graph.get_node(node_id).get_adjacents():
            if not self.marked[adjacent.get_node_id()]:
                self.pq.insert([node_id, adjacent.get_node_id()], self.compressed_graph.get_node(node_id).get_weight(adjacent))

    # essentially computed the DFS of an acyclic graph, which is the preorder traversal of a tree
    def preordertraversal(self, mst: Graph):
        self.condensed_patrol_path = []
        self.marked = {}
        self.dfs(self.mst, self.starting_node)

    def dfs(self, mst: Graph, node_id):
        self.marked[node_id] = True
        self.condensed_patrol_path.append(node_id)
        for node in mst.get_node(node_id).get_adjacents():
            if node.get_node_id() not in self.marked.keys():
                self.dfs(mst, node.get_node_id())

    def __get_mst(self):
        self.pq.queue = []
        self.__visit(self.starting_node)
        while not self.pq.is_empty():
            x = self.pq.pop()
            node = x[0][0]
            to_node = x[0][1]
            if self.marked[to_node] and self.marked[node]:
                continue
            self.mst.add_edge(node, to_node, x[1])
            if not self.marked[to_node]:
                self.__visit(to_node)
            if not self.marked[node]:
                self.__visit(node)

    def find_patrol_path(self):
        edge_combinations = list(itertools.combinations(self.nodes_to_visit, 2))
        paths_weights = {}
        for edge in edge_combinations:
            itinerary1 = Itinerary(self.graph, edge[0], edge[1], Dijkstra())
            path = itinerary1.find_shortest_path()
            paths_weights[edge] = path
            self.compressed_graph.add_edge(edge[0], edge[1], path[1])
        self.__get_mst()
        self.preordertraversal(self.mst)
        self.condensed_patrol_path.append(self.starting_node)
        for i in range(0, len(self.condensed_patrol_path)-1):
            condensed_edge = (self.condensed_patrol_path[i], self.condensed_patrol_path[i+1])
            condensed_edge_rev = (self.condensed_patrol_path[i+1], self.condensed_patrol_path[i])
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
