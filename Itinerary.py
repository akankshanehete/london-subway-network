from Graph import Graph
from ShortestPath import ShortestPath

Algorithm = ShortestPath
From = int
To = int


class Itinerary:
    def __init__(self, graph: Graph, from_station_id: From,
                 to_station_id: To, algo: Algorithm):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id

    # calls the shortest_path method using the specified algorithm (algo)
    # returns the shortest path, number of stations traversed,
    # total travel time, and lines connecting each station
    def find_shortest_path(self):
        shortest_paths = self.algo.shortest_path(self.graph,
                                                 self.from_station,
                                                 self.to_station)
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

    # prints a well-formatted itinerary
    # includes total travel time, number of stations traversed,
    # path taken, and lines connecting each station
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
