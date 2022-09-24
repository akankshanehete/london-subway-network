from abc import ABC, abstractmethod


class KPI(ABC):

    @abstractmethod
    def measurement(self, graph, algo, from_node_id, to_node_id):
        print("KPI")
        # each KPI class will provide its own implementation using this function
        pass
