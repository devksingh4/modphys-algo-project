import math

class Cluster():
    """A cluster of energy in the calorimeter"""

    def __init__(self):
        self.cal_hits = []

    def is_jet(self):
        if hasattr(self, "jet"):
            return self.jet
        else:
            return False

    def add_hit(self, hit):
        self.cal_hits.append(hit)

    def set_phi(self, phi):
        # First check the bounds for consistency
        while phi < 0:
            phi += 2 * math.pi

        while phi >= 2 * math.pi:
            phi -= 2 * math.pi

        self.phi = phi

    def set_eta(self, eta):
        self.eta = eta

    def set_energy(self, energy):
        if energy < 0:
            energy = -energy

        self.energy = energy

    def mark_jet(self):
        self.jet = True