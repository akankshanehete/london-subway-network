from Graph import Graph
from Graph_Algorithms.Dijkstra import Dijkstra
from Graph_Algorithms.A_star import A_star
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
        line_to = shortest_paths['line_to']
        path = []
        node = self.to_station
        while node != self.from_station:
            path.append(node)
            node = edge_to[node]
        path.append(self.from_station)
        node = self.to_station
        lines = []
        while node != self.from_station:
            lines.append(node)
            node = edge_to[node]
        lines.append(self.from_station)
        lines = [line_to[i] for i in lines]
        lines.pop()
        string_path = [str(i) for i in path]
        results = {}
        string_path.reverse()
        lines.reverse()
        results['path'] = string_path
        results['stations traversed'] = len(path)
        results['travel time'] = dist_to[self.to_station]
        results['lines'] = lines
        return results
        # return "Travel time: " + str(dist_to[self.to_station]) + "\n" + " -> ".join(reversed(string_path)) + "\nStations traversed: " + str(len(path)), len(path)
        # return self.algo.shortest_path(self.graph, self.from_station, self.to_station)

    def print_itinerary(self):
        results = self.find_shortest_path()
        print("Itinerary:")
        print("Travel time is " + str(results['travel time']) + ".")
        print(str(results['stations traversed']) + " stations traversed.")
        path = results['path']
        lines = [" --" + i + "--> " for i in results['lines']]
        string_path = [None]*(len(path)+len(lines))
        string_path[::2] = path
        string_path[1::2] = lines
        print("".join(string_path))



