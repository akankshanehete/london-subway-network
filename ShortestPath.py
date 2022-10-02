from abc import ABC, abstractmethod
from Graph import Graph

From = int
To = int


class ShortestPath(ABC):

    @abstractmethod
    def shortest_path(self, graph: Graph, from_node_id: From, to_node_id: To):
        # each shortest path class will provide its own implementation
        # using this function
        pass

    @abstractmethod
    def get_name(self):
        # each shortest path class with provide its own implementation
        # using this function
        pass
