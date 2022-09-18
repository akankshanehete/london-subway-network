"""
this class reads files and extracts information, storing the results in a dictionary data structure
for easy access to key value pairs
"""

class Csv_reader:
    def __init__(self):
        pass

    def csv_to_list(self, csv_text):
        rows = []
        lines = csv_text.readlines()
        for line in lines:
            rows.append(line.split(","))
        rows.pop(0)
        return rows


    def extract_stations(self, filename):
        stations_file = open(filename, 'r')
        stations_file = self.csv_to_list(stations_file)
        stations = []
        for i in stations_file:
            station = {'id': i[0], 'lat': i[1], 'long': i[2], 'name': i[3], 'display name': i[4], 'zone': i[5], 'total lines': i[6], 'rail': i[7].strip('\n')}
            stations.append(station)
        return stations


    def extract_lines(self, filename):
        lines_file = open(filename, 'r')
        lines_file = self.csv_to_list(lines_file)
        lines = []
        for i in lines_file:
            line = {'line': i[0], 'name': i[1], 'colour': i[2], 'stripe': i[3].strip('\n')}
            lines.append(line)
        return lines


    def extract_connections(self,filename):
        connections_file = open(filename, 'r')
        connections_file = self.csv_to_list(connections_file)
        connections = []
        for i in connections_file:
            connection = {'s1': i[0], 's2': i[1], 'line': i[2], 'time': i[3].strip('\n')}
            connections.append(connection)
        return connections


