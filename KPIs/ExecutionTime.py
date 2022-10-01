import time
from KPI import KPI


class ExecutionTime(KPI):

    def measurement(self, graph, algo, from_node_id, to_node_id):
        start_time = time.time()
        algo.shortest_path(graph, from_node_id, to_node_id)
        end_time = time.time()
        return end_time - start_time
