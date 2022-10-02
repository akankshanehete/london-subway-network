from Graph import Graph
from ShortestPath import ShortestPath
from KPI import KPI

Algorithm = ShortestPath
From = int
To = int


class Test:
    def __init__(self, graph: Graph, algo: Algorithm, kpi: KPI,
                 from_station_id: From, to_station_id: To):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id
        self.kpi = kpi

    # calls the measurement function based on the specified KPI
    def find_measurement(self):
        return self.kpi.measurement(self.graph, self.algo,
                                    self.from_station, self.to_station)
