import time
from KPI import KPI


class CpuTime(KPI):

    def measurement(self, graph, algo, from_node_id, to_node_id):
        start_time = time.process_time()
        algo.shortest_path(graph, from_node_id, to_node_id)
        end_time = time.process_time()
        return end_time - start_time
