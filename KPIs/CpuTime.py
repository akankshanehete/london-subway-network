import time
from KPI import KPI
from Graph import Graph
from ShortestPath import ShortestPath

Algorithm = ShortestPath
From = int
To = int


class CpuTime(KPI):

    # measures time at start and end of algorithm execution
    # returns the difference
    def measurement(self, graph: Graph, algo: Algorithm,
                    from_node_id: From, to_node_id: To):
        start_time = time.process_time()
        algo.shortest_path(graph, from_node_id, to_node_id)
        end_time = time.process_time()
        return 1000 * (end_time - start_time)
