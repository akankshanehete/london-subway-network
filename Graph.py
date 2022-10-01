from Node import Node

# creates a graph object
class Graph:
    def __init__(self):
        self.num_nodes = 0
        self.num_edges = 0
        self.all_nodes = {}

    # makes graph object iterable
    def __iter__(self):
        return iter(self.all_nodes.values())

    # adds node to graph
    def add_node(self, node: Node):
        self.num_nodes += 1
        self.all_nodes[node.get_node_id()] = node
        return node

    # given node id, this function gets a node
    def get_node(self, node):
        if node in self.all_nodes:
            return self.all_nodes[node]
        else:
            return None

    # adds an edge where the default weight is 0 unless a specific number is specified
    def add_edge(self, from_node, to_node, weight=0, label = ''):
        if from_node not in self.all_nodes:
            f = Node(from_node)
            self.add_node(f)
        if to_node not in self.all_nodes:
            t = Node(to_node)
            self.add_node(t)
        self.all_nodes[from_node].add_adjacent(self.all_nodes[to_node], weight, label)
        self.all_nodes[to_node].add_adjacent(self.all_nodes[from_node], weight, label)
        self.num_edges += 1

    # checks if there is a given edge between 2 node ids in graph
    def is_edge(self, from_node, to_node):
        if from_node not in self.all_nodes:
            return False
        if to_node not in self.all_nodes:
            return False
        if (self.get_node(from_node) in self.get_node(to_node).get_adjacents()) and self.get_node(to_node) in self.get_node(from_node).get_adjacents():
            return True
        return False

    # deletes edge from graph if edge is present in graph
    def delete_edge(self, from_node, to_node):
        if from_node not in self.all_nodes or to_node not in self.all_nodes:
            raise Exception("One or both of these nodes are not contained in the graph. Please enter nodes that are contained in the graph.")
        self.all_nodes[from_node].del_adjacent(self.all_nodes[to_node])
        self.all_nodes[to_node].del_adjacent(self.all_nodes[from_node])
        self.num_edges -= 1

    # gets the maximum weight from the graph
    def get_max_weight(self):
        max = 0
        all_nodes = list(self.all_nodes)
        for node in all_nodes:
            for adj in self.get_node(node).get_adjacents():
                temp = self.get_node(node).get_weight(adj)
                if temp > max:
                    max = temp
        return max

    # prints all connections in the graph, along with their weight and label (if the label exists)
    def print_all_connections(self):
        for node in self:
            for neighbour in node.get_adjacents():
                node_id = node.get_node_id()
                neighbour_id = neighbour.get_node_id()
                print('( %s , %s, %3d, %s)' % (node_id, neighbour_id, node.get_weight(neighbour), node.get_label(neighbour)))



