from Station_Node import Station_Node
from Graph import Graph
from Csv_reader import Csv_reader


class Graph_builder:
    def __init__(self, csv: Csv_reader, graph: Graph):
        self.csv_reader = csv
        self.stations = None
        self.lines = None
        self.connections = None
        self.graph = graph

    # creates nodes in the graph from stations
    def create_station_nodes(self, stations_file):
        self.stations = self.csv_reader.extract_csv(stations_file)
        for station in self.stations:
            station_node = Station_Node(int(station['id']),
                                        station['display_name'])
            station_node.set_lat(float(station['latitude']))
            station_node.set_long(float(station['longitude']))
            station_node.set_zone(station['zone'])
            station_node.set_disp_name(station['display_name'])
            station_node.set_total_lines(station['total_lines'])
            station_node.set_is_rail(int(station['rail']))
            self.graph.add_node(station_node)

    # creates connections in the graph from connections
    def create_connections(self, connections_file):
        self.connections = self.csv_reader.extract_csv(connections_file)
        for connection in self.connections:
            self.graph.add_edge(int(connection['station1']),
                                int(connection['station2']),
                                int(connection['time']),
                                connection['line'])
