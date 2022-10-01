
class Test:
    def __init__(self, graph, algo, kpi, from_station_id, to_station_id):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id
        self.kpi = kpi

    def find_measurement(self):
        return self.kpi.measurement(self.graph, self.algo, self.from_station, self.to_station)
