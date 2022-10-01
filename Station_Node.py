from Node import Node

ID = int
Name = str
Latitude = float
Longitude = float
Zone = int
Lines = int
Rail = int


# class station node is a node, i.e. extends the node class
# contains properties of a regular node but adds on station properties
class Station_Node(Node):
    def __init__(self, node_id: ID, name: Name):
        super().__init__(self)
        self.id = node_id
        self.name = name
        self.lat = None
        self.long = None
        self.disp_name = None
        self.zone = None
        self.total_lines = None
        self.is_rail = None

    def set_lat(self, lat: Latitude):
        self.lat = lat

    def set_long(self, long: Longitude):
        self.long = long

    def set_disp_name(self, disp: Name):
        self.disp_name = disp

    def set_zone(self, zone: Zone):
        self.zone = zone

    def set_total_lines(self, total_lines: Lines):
        self.total_lines = total_lines

    def set_is_rail(self, is_rail: Rail):
        self.is_rail = is_rail
