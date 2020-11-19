import math

class Track:
    """A particle track"""

    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def set_vertex(self, vertex):
        self.vertex = vertex

    def set_phi(self, phi):
        # First check the bounds for consistency
        while phi < 0:
            phi += 2 * math.pi

        while phi >= 2 * math.pi:
            phi -= 2 * math.pi

        self.phi = phi

    def set_eta(self, eta):
        self.eta = eta

    def set_pT(self, pT):
        if pT < 0:
            pT = -pT

        self.pT = pT
            

