from KPI import KPI


class Visited(KPI):

    def measurement(self, graph, algo, from_node_id, to_node_id):
        return algo.shortest_path(graph, from_node_id, to_node_id)['visited']
