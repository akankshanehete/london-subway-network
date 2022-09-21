from Node import Node
from Station_Node import Station_Node
from Graph import Graph
from Csv_reader import Csv_reader

class Graph_builder:
    def __init__(self, csv : Csv_reader, graph : Graph):
        self.csv_reader = csv
        self.stations = None
        self.lines = None
        self.connections = None
        self.graph = graph

    # creates nodes in the graph from stations
    def create_station_nodes(self, stations_file):
        self.stations = self.csv_reader.extract_stations(stations_file)
        for station in self.stations:
            station_node = Station_Node(int(station['id']), station['name'])
            station_node.set_lat(float(station['lat']))
            station_node.set_long(float(station['long']))
            station_node.set_zone(station['zone'])
            station_node.set_disp_name(station['display name'])
            station_node.set_total_lines(station['total lines'])
            station_node.set_is_rail(int(station['rail']))
            self.graph.add_node(station_node)


    def create_connections(self, connections_file):
        self.connections = self.csv_reader.extract_connections(connections_file)
        for connection in self.connections:
            self.graph.add_edge(int(connection['s1']), int(connection['s2']), int(connection['time']), connection['line'])



