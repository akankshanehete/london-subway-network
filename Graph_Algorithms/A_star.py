from Graph import Graph
from ShortestPath import ShortestPath
from Node import Node
from Station_Node import Station_Node
import math
from Graph_Algorithms.Priority_Queue import PriorityQueue


class A_star(ShortestPath):

    def shortest_path(self, graph, from_node_id, to_node_id):
        shortest_paths = self.A_star(graph, from_node_id, to_node_id)
        edge_to = shortest_paths[0]
        dist_to = shortest_paths[1]
        path = []
        node = to_node_id
        while node != from_node_id:
            path.append(node)
            node = edge_to[node]
        path.append(from_node_id)
        print("shortest path length = ", dist_to[to_node_id])
        string_path = [str(i) for i in path]
        print(" -> ".join(reversed(string_path)))
    def A_star(self, graph: Graph, from_node_id, to_node_id):
        # provide A* implementation here
        unvisited = PriorityQueue()
        unvisited.insert(from_node_id, graph.get_max_weight() + distance(graph, graph.get_node(from_node_id), graph.get_node(to_node_id)))
        edge_to = {}
        dist_to = {}
        edge_to[from_node_id] = None
        dist_to[from_node_id] = 0
        while not unvisited.is_empty():
            current = unvisited.pop()[0]
            if current == to_node_id:
                break
            adjacent = graph.get_node(current).get_adjacents()
            for adj in adjacent:
                temp = dist_to[current] + graph.get_node(current).get_weight(adj)
                a = adj.get_node_id()
                if adj not in dist_to or temp < dist_to[a]:
                    dist_to[a] = temp
                    edge_to[a] = current
                    unvisited.insert(a, graph.get_max_weight() - graph.get_node(current).get_weight(adj) + distance(graph, graph.get_node(a), graph.get_node(to_node_id)))
        return edge_to, dist_to


def distance(graph: Graph, from_node_id: Station_Node, to_node_id: Station_Node):
    x = abs(from_node_id.lat - to_node_id.lat)
    y = abs(from_node_id.long - to_node_id.long)
    return math.sqrt(x * x + y * y)
