class Node:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    # adds adjacent node id to this node's adjacency list
    def add_adjacent(self, adjacent_node, weight=0, label=''):
        self.adjacent[adjacent_node] = [weight, label]

    # deletes adjacent node id from this node's adjacency list
    def del_adjacent(self, adjacent_node):
        self.adjacent.pop(adjacent_node)

    # gets this node's adjacency list
    def get_adjacents(self):
        return self.adjacent.keys()

    # gets this node's id (each id is unique to the node)
    def get_node_id(self):
        return self.id

    # gets the weight of the edge connecting this node to one of its adjacent nodes
    def get_weight(self, adjacent_node):
        return self.adjacent[adjacent_node][0]

    # gets the label of the edge connecting this node to one of its adjacent nodes
    def get_label(self, adjacent_node):
        return self.adjacent[adjacent_node][1]
