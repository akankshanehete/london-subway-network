from KPI import KPI


class Inserts(KPI):

    def measurement(self, graph, algo, from_node_id, to_node_id):
        return algo.shortest_path(graph, from_node_id, to_node_id)['inserts']
