class MatchedObjects():
    """Tracks, clusters, and muon stubs that may be matched together"""

    def add_track(self, track):
        self.track = track

    def add_cluster(self, cluster):
        self.cluster = cluster

    def add_muon_stub(self, muon_stub):
        self.muon_stub = muon_stub

    def has_track(self):
        return hasattr(self, "track")

    def has_cluster(self):
        return hasattr(self, "cluster")

    def has_muon_stub(self):
        return hasattr(self, "muon_stub")

    def has_any_match(self):
        return (self.has_track() and self.has_cluster()) or (self.has_track() and self.has_muon_stub()) or (self.has_cluster() and self.has_muon_stub())

    def can_merge(self, other):
        if (hasattr(self, "track") and hasattr(other, "track")):
            return self.track is other.track
        else:
            return False

    def merge(self, other):
        new_matched_objects = MatchedObjects()

        if not self.can_merge(other):
            return

        self.merge_specific(other, new_matched_objects, "cluster")
        self.merge_specific(other, new_matched_objects, "muon_stub")

        return new_matched_objects


    def merge_specific(self, other, matched_objects, attribute):
        if not self.can_merge(other):
            raise Exception("Attempted to merge unmergeable objects!")

        if hasattr(self, attribute) and hasattr(other, attribute):
            if getattr(self, attribute) is getattr(other, attribute):
                matched_objects.track = self.track
                setattr(matched_objects, attribute, getattr(self, attribute))
            else:
                raise Exception("Differing attributes for same track!")
        elif hasattr(self, attribute):
            matched_objects.track = self.track
            setattr(matched_objects, attribute, getattr(self, attribute))
        elif hasattr(other, attribute):
            matched_objects.track = self.track
            setattr(matched_objects, attribute, getattr(other, attribute))
        
        return matched_objects

    def print_matches(self):
        if (self.has_any_match()):
            line = "Matched "
            if (self.has_track()):
                line += "track with pT " + str(self.track.pT) + " with "
            if (self.has_cluster()):
                line += "cluster with energy " + str(self.cluster.energy) + " with "
            if (self.has_muon_stub()):
                if len(self.muon_stub.hits) > 0:
                    line += "muon stub with point { " + str(self.muon_stub.hits[0].x) + ", " + str(self.muon_stub.hits[0].y) + ", " + str(self.muon_stub.hits[0].z) + " }" 
            print(line)

