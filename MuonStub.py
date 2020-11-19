class MuonStub():
    """A signature of a muon found in the muon detector"""

    def __init__(self):
        self.hits = []

    def add_point(self, hit):
        self.hits.append(hit)
        

