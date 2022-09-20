
class Itinerary:
    def __init__(self, graph, from_station_id, to_station_id, algo):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id

    def find_shortest_path(self):
        shortest_paths = self.algo.shortest_path(self.graph, self.from_station, self.to_station)
        edge_to = shortest_paths[0]
        dist_to = shortest_paths[1]
        path = []
        node = self.to_station
        while node != self.from_station:
            path.append(node)
            node = edge_to[node]
        path.append(self.from_station)
        string_path = [str(i) for i in path]
        return "Travel time: " + str(dist_to[self.to_station]) + "\n" + " -> ".join(reversed(string_path))
        # return self.algo.shortest_path(self.graph, self.from_station, self.to_station)
