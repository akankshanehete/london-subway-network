# creates a node in the graph
class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.adjacent = {}

    def add_adjacent(self, adjacent_node, weight=0, label =''):
        self.adjacent[adjacent_node] = [weight,label]

    def get_adjacents(self):
        return self.adjacent.keys()

    def get_node_id(self):
        return self.id

    def get_weight(self, adjacent_node):
        return self.adjacent[adjacent_node][0]

    def get_label(self, adjacent_node):
        return self.adjacent[adjacent_node][1]