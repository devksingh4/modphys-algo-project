from CalorimeterHit import CalorimeterHit
from EventReadout import EventReadout
from Cluster import Cluster
from MuonStub import MuonStub
from Vector import Vector
from Track import Track

class FileReader():
    """A class to read in a text file and convert it to an EventReadout format"""

    def get_event(self, filename):
        with (open(filename, "r")) as file:
            # Clear off the header row
            file.readline()
            event_readout = EventReadout()

            while self.get_one_hit(file, event_readout):
                pass

        return event_readout

    def get_one_hit(self, file, event_readout):
        line = file.readline()
        if not line:
            return False

        self.read_line(line, event_readout)

        return True

    def read_line(self, line, event_readout):
        numbers = line.split("\t")

        position = Vector(numbers[0], numbers[1], numbers[2])

        if len(numbers) > 3:
            energy = numbers[3]
            cal_hit = CalorimeterHit(position, energy)
            event_readout.add_calorimeter_hit(cal_hit)
        else:
            event_readout.add_tracker_hit(position)

    def get_all_particles_in_event(self, filename):
        events = []

        with (open(filename, "r")) as file:

            line = file.readline() # Should be "Next particle"
            if line != "Next particle\n":
                return
            complete = False
            while not complete:
                file.readline() # Remove header
                event, complete = self.get_one_particle(file)
                events.append(event)
        return events

    def get_one_particle(self, file):
        event_readout = EventReadout()

        line = file.readline()
        while line != "Next particle\n" and line:
            self.read_line(line, event_readout)
            line = file.readline()
        
        return event_readout, (line == "")

    def get_all_tracks(self, filename):
        events = self.get_all_particles_in_event(filename)
        tracks = []
        for event in events:
            track = Track()
            for hit in event.tracker_hits:
                if (hit.magnitude() < 5):
                    track.add_point(hit)
            tracks.append(track)

        return tracks

    def get_all_clusters(self, filename):
        events = self.get_all_particles_in_event(filename)
        clusters = []
        for event in events:
            cluster = Cluster()
            for hit in event.calorimeter_hits:
                cluster.add_hit(hit)
            clusters.append(cluster)

        return clusters

    def get_all_muon_stubs(self, filename):
        events = self.get_all_particles_in_event(filename)
        muon_stubs = [] 
        for event in events:
            muon_stub = MuonStub()
            for hit in event.tracker_hits:
                if (hit.magnitude() > 5):
                    muon_stub.add_point(hit)
            #if len(muon_stub.hits) > 0:
            muon_stubs.append(muon_stub)

        return muon_stubs