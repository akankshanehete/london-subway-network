from Node import Node

# class station node is a node, i.e extends the node class
# contains properties of a regular node but adds on station properties
class Station_Node(Node):
    def __init__(self, id, name:str):
        super().__init__(self)
        self.id = id
        self.name = name
        self.lat = None
        self.long = None
        self.disp_name = None
        self.zone = None
        self.total_lines = None
        self.is_rail = None

    def set_lat(self, lat):
        self.lat = lat

    def set_long(self, long):
        self.long = long

    def set_disp_name(self, disp):
        self.disp_name = disp

    def set_zone(self, zone):
        self.zone = zone

    def set_total_lines(self, total_lines):
        self.total_lines = total_lines

    def set_is_rail(self, is_rail):
        self.is_rail = is_rail

