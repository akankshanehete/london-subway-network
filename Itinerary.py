

class Itinerary:
    def __init__(self, graph, from_station_id, to_station_id,algo):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id


    def find_shortest_path(self):
        return self.algo.shortest_path(self.graph, self.from_station, self.to_station)

