from Node import Node

# creates a graph
class Graph:
    def __init__(self):
        self.num_nodes = 0
        self.num_edges = 0
        self.all_nodes = {}

    def __iter__(self):
        return iter(self.all_nodes.values())

    def add_node(self, node: Node):
        self.num_nodes += 1
        self.all_nodes[node.get_node_id()] = node
        return node

    def get_node(self, node):
        if node in self.all_nodes:
            return self.all_nodes[node]
        else:
            return None

    # adds an edge where the default weight is 0 unless a specific number is specified
    def add_edge(self, from_node, to_node, weight=0, label = ''):
        if from_node not in self.all_nodes:
            self.add_node(Node(from_node))
        if to_node not in self.all_nodes:
            self.add_node(Node(to_node))

        self.all_nodes[from_node].add_adjacent(self.all_nodes[to_node], weight,label)
        self.all_nodes[to_node].add_adjacent(self.all_nodes[from_node], weight,label)
        self.num_edges += 1

    def get_max_weight(self):
        max = 0
        all_nodes = list(self.all_nodes)
        for node in all_nodes:
            for adj in self.get_node(node).get_adjacents():
                temp = self.get_node(node).get_weight(adj)
                if temp > max:
                    max = temp
        return max

    #prints all connectionsin the graph
    def print_all_connections(self):
        for node in self:
            for neighbour in node.get_adjacents():
                node_id = node.get_node_id()
                neighbour_id = neighbour.get_node_id()
                print('( %s , %s, %3d, %s)' % (node_id, neighbour_id, node.get_weight(neighbour), node.get_label(neighbour)))





