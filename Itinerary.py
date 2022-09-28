from Graph import Graph
from Graph_Algorithms.Dijkstra import Dijkstra
class Itinerary:
    def __init__(self, graph, from_station_id, to_station_id, algo):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id

    def find_shortest_path(self):
        shortest_paths = self.algo.shortest_path(self.graph, self.from_station, self.to_station)
        edge_to = shortest_paths['edge_to']
        dist_to = shortest_paths['dist_to']
        path = []
        node = self.to_station
        while node != self.from_station:
            path.append(node)
            node = edge_to[node]
        path.append(self.from_station)
        string_path = [int(i) for i in path]
        string_path.reverse()
        total_weight = dist_to[self.to_station]
        return string_path, total_weight

