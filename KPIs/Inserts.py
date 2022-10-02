from KPI import KPI
from Graph import Graph
from ShortestPath import ShortestPath

Algorithm = ShortestPath
From = int
To = int


class Inserts(KPI):

    # returns 'inserts' value from shortest_path output
    def measurement(self, graph: Graph, algo: Algorithm,
                    from_node_id: From, to_node_id: To):
        return algo.shortest_path(graph, from_node_id, to_node_id)['inserts']
