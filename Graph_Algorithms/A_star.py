from Graph import Graph
from ShortestPath import ShortestPath
from Node import Node
from Station_Node import Station_Node
import math
from Graph_Algorithms.Priority_Queue import PriorityQueue


class A_star(ShortestPath):
    def shortest_path(self, graph: Graph, from_node_id, to_node_id):
        # provide A* implementation here
        unvisited = PriorityQueue()
        unvisited.insert(from_node_id, - distance(graph.get_node(from_node_id), graph.get_node(to_node_id)))
        results = {}
        edge_to = {}
        dist_to = {}
        inserts = 0
        visited = 0
        compares = 0
        for i in graph.all_nodes:
            dist_to[i] = float('inf')
        edge_to[from_node_id] = None
        dist_to[from_node_id] = 0
        while not unvisited.is_empty():
            visited += 1
            current = unvisited.pop()[0]
            if current == to_node_id:
                break
            adjacent = graph.get_node(current).get_adjacents()
            for adj in adjacent:
                temp = dist_to[current] + graph.get_node(current).get_weight(adj)
                a = adj.get_node_id()
                compares += 1
                if a not in edge_to or temp < dist_to[a]:
                    dist_to[a] = temp
                    edge_to[a] = current
                    inserts += 1
                    unvisited.insert(a, temp + 20*distance(graph.get_node(a), graph.get_node(to_node_id)))
        results['edge_to'] = edge_to
        results['dist_to'] = dist_to
        results['inserts'] = inserts
        results['visited'] = visited
        results['compares'] = compares
        return results

    def get_name(self):
        return "A_star"


def distance(from_node_id: Station_Node, to_node_id: Station_Node):
    x = abs(from_node_id.lat - to_node_id.lat)
    y = abs(from_node_id.long - to_node_id.long)
    return math.sqrt(x * x + y * y)
