from Graph import Graph
from ShortestPath import ShortestPath
from Station_Node import Station_Node
import math
from Graph_Algorithms.Priority_Queue import PriorityQueue

From = int
To = int


class A_star(ShortestPath):
    def shortest_path(self, graph: Graph, from_node_id: From, to_node_id: To):
        const = 10
        unvisited = PriorityQueue()
        unvisited.insert(from_node_id,
                         - self.distance(graph.get_node(from_node_id),
                                         graph.get_node(to_node_id)))
        results = {}
        edge_to = {}
        dist_to = {}
        line_to = {}
        inserts = 0
        visited = 0
        compares = 0
        # initialize all distances to inf
        for i in graph.all_nodes:
            dist_to[i] = float('inf')
        edge_to[from_node_id] = None
        dist_to[from_node_id] = 0
        line_to[from_node_id] = None
        # visit nodes based on priority
        # relax edge_to if shorter dist_to is found
        while not unvisited.is_empty():
            current = unvisited.pop()[0]
            visited += 1
            if current == to_node_id:
                break
            adjacent = graph.get_node(current).get_adjacents()
            for adj in adjacent:
                temp = dist_to[current] \
                       + graph.get_node(current).get_weight(adj)
                a = adj.get_node_id()
                if a not in edge_to or temp < dist_to[a]:
                    compares += 1
                    dist_to[a] = temp
                    edge_to[a] = current
                    line_to[a] = graph.get_node(current).get_label(adj)
                    # set priority using temp and distance heuristic
                    weight = temp
                    weight += const * self.distance(graph.get_node(a),
                                                    graph.get_node(to_node_id))
                    unvisited.insert(a, weight)
                    inserts += 1
                else:
                    compares += 1
        # return all values and KPIs as dictionary
        results['edge_to'] = edge_to
        results['dist_to'] = dist_to
        results['line_to'] = line_to
        results['inserts'] = inserts
        results['visited'] = visited
        results['compares'] = compares
        return results

    # A* heuristic takes the physical distance of the current node to the
    # destination node as higher priority. Distance is then multiplied by
    # const which determines how much the heuristic affects priority
    @staticmethod
    def distance(from_node: Station_Node, to_node: Station_Node):
        x = abs(from_node.lat - to_node.lat)
        y = abs(from_node.long - to_node.long)
        return math.sqrt(x * x + y * y)

    def get_name(self):
        return "A_star"
