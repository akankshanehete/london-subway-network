from Graph import Graph
from Plotter import Plotter

ID = int


class Metric_Extractor:
    def __init__(self, graph: Graph):
        self.graph = graph

    def get_node_count(self):
        return self.graph.num_nodes

    def get_edge_count(self):
        return self.graph.num_edges

    def get_degree(self, node: ID):
        return len(self.graph.get_node(node).adjacent)

    def get_avg_degree(self):
        return float(2*self.graph.num_edges/self.graph.num_nodes)

    def plot_node_dist(self):
        degree_list = []
        for node in self.graph:
            degree_list.append(self.get_degree(node.id))

        maximum = max(degree_list)
        node_distribution_list = []
        for i in range(0, maximum):
            node_distribution_list.append(degree_list.count(i))
        distribution_plot = Plotter()
        distribution_plot.plot(node_distribution_list,
                               'Graph Node Distribution',
                               'Degree',
                               'Number of Nodes')
