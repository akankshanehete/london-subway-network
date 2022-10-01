from Graph import Graph


class ConnectedComponents:
    def __init__(self):
        self.marked = {}
        self.graph = Graph()
        self.connected_components = []
        self.cc = []

    def get_connected_components(self, graph: Graph):
        self.marked = {}
        self.graph = graph
        for node in self.graph:
            self.marked[node.get_node_id()] = False
        for node in self.graph:
            if not self.marked[node.get_node_id()]:
                self.cc = []
                cc = self.dfs(node.get_node_id())
                self.connected_components.append(cc)
        return self.connected_components

    def dfs(self, node_id):
        self.marked[node_id] = True
        self.cc.append(node_id)
        for node in self.graph.get_node(node_id).get_adjacents():
            if not self.marked[node.get_node_id()]:
                self.dfs(node.get_node_id())
        return self.cc


# testgraph = Graph()
# testgraph.add_edge(23, 12)
# testgraph.add_edge(12, 4)
# testgraph.add_edge(9, 13)
# testgraph.add_edge(9, 87)
# connected_comp = ConnectedComponents()
# components = connected_comp.get_connected_components(testgraph)
# print(components)
