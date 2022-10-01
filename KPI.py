from abc import ABC, abstractmethod
from Graph import Graph
from ShortestPath import ShortestPath

Algorithm = ShortestPath
From = int
To = int


class KPI(ABC):

    @abstractmethod
    def measurement(self, graph: Graph, algo: Algorithm, from_node_id: From, to_node_id: To):
        # each KPI class will provide its own implementation using this function
        pass
