class EventReadout():
    """A full readout of the raw hits in the event"""

    def __init__(self):
        self.tracker_hits = []
        self.calorimeter_hits = []

    def add_tracker_hit(self, position):
        self.tracker_hits.append(position)

    def add_calorimeter_hit(self, calHit):
        self.calorimeter_hits.append(calHit)
