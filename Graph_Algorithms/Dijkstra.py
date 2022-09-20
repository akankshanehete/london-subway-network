from Graph import Graph
from ShortestPath import ShortestPath
from Graph_Algorithms.Priority_Queue import PriorityQueue


class Dijkstra(ShortestPath):

    def shortest_path(self, graph: Graph, from_node_id, to_node_id):
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
