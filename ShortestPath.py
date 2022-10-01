from abc import ABC, abstractmethod


class ShortestPath(ABC):

    @abstractmethod
    def shortest_path(self, graph, from_node_id, to_node_id):
        # each shortest path class will provide its own implementation using this function
        pass

    @abstractmethod
    def get_name(self):
        # each shortest path class with provide its own implementation using this function
        pass




