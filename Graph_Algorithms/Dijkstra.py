from Graph import Graph
from ShortestPath import ShortestPath
import math
from Graph_Algorithms.Priority_Queue import PriorityQueue


class Dijkstra(ShortestPath):

    def shortest_path(self, graph, from_node_id, to_node_id):
        shortest_paths = self.dijkstra2(graph, from_node_id, to_node_id)
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

    def dijkstra(self, graph: Graph, from_node_id):
        unvisited = list(graph.all_nodes)
        dist_to = {}
        edge_to = {}
        for i in unvisited:
            dist_to[i] = math.inf
        dist_to[from_node_id] = 0
        while unvisited:
            current = None
            for i in unvisited:
                if current is None:
                    current = i
                elif dist_to[i] < dist_to[current]:
                    current = i
            adjacent = graph.get_node(current).get_adjacents()
            for adj in adjacent:
                temp = dist_to[current] + graph.get_node(current).get_weight(adj)
                a = adj.get_node_id()
                if temp < dist_to[a]:
                    dist_to[a] = temp
                    edge_to[a] = current
            unvisited.remove(current)
        return edge_to, dist_to

    def dijkstra2(self, graph: Graph, from_node_id, to_node_id):
        unvisited = PriorityQueue()
        unvisited.insert(from_node_id, graph.get_max_weight())
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
                    unvisited.insert(a, graph.get_max_weight() - graph.get_node(current).get_weight(adj))
        return edge_to, dist_to